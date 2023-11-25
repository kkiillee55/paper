import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables
_ = load_dotenv(find_dotenv())

from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader, PyPDFLoader, DirectoryLoader, TextLoader, UnstructuredPDFLoader
from langchain.vectorstores import DocArrayInMemorySearch
from IPython.display import display, Markdown
from langchain.indexes import VectorstoreIndexCreator


# Initialize OpenAI embeddings
embeddings = OpenAIEmbeddings()

# Setup the loader for PDF documents in a directory
loader = DirectoryLoader('content/data_pdf/', glob="**/*.pdf", loader_cls=PyPDFLoader)

# Load documents
documents = loader.load()

# Print document metadata
for doc in documents:
    print(doc.metadata['source'])
    print(doc.metadata['page'])

# Count the number of documents
print("Number of documents loaded:", len(documents))


# # Create an index for the loaded documents
index = VectorstoreIndexCreator(
    vectorstore_cls=DocArrayInMemorySearch
).from_loaders([loader])

# Query the index
query = "please tell me how to authenticate Cypress run"
response = index.query(query)

# Display the response
display(Markdown(response))
