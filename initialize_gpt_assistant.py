from enum import  Enum

from langchain.document_loaders import WebBaseLoader
from langchain.memory import ConversationSummaryMemory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from gpt_researcher import GPTResearcher
import asyncio
from langchain.document_loaders import PyPDFLoader

class ResearchField(Enum):
    COMPUTER_SCIENCE=1
    UNKNOWN=2

def _extract_research_field() -> ResearchField:
    """Extract research field from research paper.
    Args:
    Returns:
        ResearchField enum.
    """
    return ResearchField.COMPUTER_SCIENCE

def _extract_keywords() -> list[str]:
    """Extract keywords form the paper.

    Args:
    Returns:
        A list of keywords
    """
    return []

def _extract_citations() -> list[str]:
    """Extract citations from the paper.

    Args:
    Returns:
        A list of citations
    """
    return []

def _extract_title() -> str:
    """Extract title from the paper.
    Args:
    Returns:
        The research title.
    """
    return ""

async def _search(questions: list[str], report_type="resource_report") -> dict[str,str]:
    """Search questions using GPT-Researcher.

    Args:
        questions: a list of questions.
    Returns:
        A dict of question -> search result.
    """
    search_result = {}
    for query in questions:
        researcher = GPTResearcher(query=query, report_type=report_type, config_path=None)
        report = asyncio.run(researcher.run())
        search_result[query]=report
    return search_result

#TODO(@irene1391) Implementation.
def _create_model(research_field:ResearchField,search_results:dict[str,str]) -> ConversationalRetrievalChain:
    """Generate a LLM model with embeddings.

    Args:
        research_field: the research field of user uploaded PDF, we need this to load latest research progress as embedding.
        search_results: the search result of keyword/citations/title, we need this for embedding as well.
    Returns:
        A chain.
    """
    #Code copied from langchain chatbot exmpale, need to change it.
    loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    all_splits = text_splitter.split_documents(data)
    vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())

    llm = ChatOpenAI()
    retriever = vectorstore.as_retriever()
    memory = ConversationSummaryMemory(
        llm=llm, memory_key="chat_history", return_messages=True
    )
    return ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory)
    #raise NotImplementedError


def create_model(path:str) -> ConversationalRetrievalChain:
    """Generate a LLM model from user uploaded PDF.

    Args:
        path: path of research paper uploaded by user.
    Returns:
        Chatbot
    """
    research_field = _extract_research_field()
    keywords = _extract_keywords()
    citations = _extract_citations()
    questions = []
    questions.extend([f"What is {keyword}" for keyword in keywords])
    questions.extend([f"Summarize {citation}" for citation in citations])

    loader = PyPDFLoader(path)
    pages = loader.load_and_split()
    paper = ''.join([p.page_content for p in pages])
    if paper:
        questions.append(f"Can you summarize this paper? {paper}")

    search_result = _search(questions)
    return _create_model(research_field,search_result)

def dummy_create_model():
    loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    all_splits = text_splitter.split_documents(data)
    vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())

    llm = ChatOpenAI()
    retriever = vectorstore.as_retriever()
    memory = ConversationSummaryMemory(
        llm=llm, memory_key="chat_history", return_messages=True
    )
    return ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory)