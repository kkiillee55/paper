import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables
_ = load_dotenv(find_dotenv())

from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader, PyPDFLoader, DirectoryLoader, TextLoader, UnstructuredPDFLoader
from IPython.display import display, Markdown
from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.text_splitter import RecursiveCharacterTextSplitter
import glob



# Initialize OpenAI embeddings
embeddings = OpenAIEmbeddings()

# Setup the loader for PDF documents in a directory
# loader = DirectoryLoader('content/data_pdf/', glob="**/*.pdf", loader_cls=PyPDFLoader)

# Directory containing PDF files
directory = 'content/data_pdf/'

# Find all PDF files in the directory
pdf_files = glob.glob(f'{directory}/**/*.pdf', recursive=True)

# Load each PDF file using PyPDFLoader and store the results in an array
loader = [PyPDFLoader(pdf_file) for pdf_file in pdf_files]

# Load documents
docs = []
for l in loader:
    docs.extend(l.load())
text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000)
docs = text_splitter.split_documents(docs)

# Print document metadata
for doc in docs:
    print(doc.metadata['source'])
    print(doc.metadata['page'])

# Count the number of documents
print("Number of documents loaded:", len(docs))


# # Create an index for the loaded documents
index = VectorstoreIndexCreator(
    vectorstore_cls=DocArrayInMemorySearch
).from_loaders([loader])
db = DocArrayInMemorySearch.from_documents(docs, embeddings)




# Query the index
query = "please tell me how to authenticate Cypress run"
response = db.similarity_search(query)

# Display the response
display(Markdown(response))
