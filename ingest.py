from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader=PyPDFLoader("Insurance_Handbook.pdf")
documents=loader.load()
text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000
                                             ,chunk_overlap=50)
texts=text_splitter.split_documents(documents)

#load the embedding model
model_name="BAAI/bge-base-en-v1.5"
model_kwargs={'device':'cpu'}
encode_kwargs={'normalize_embeddings':False} 

embeddings=HuggingFaceBgeEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

print("Embedding Model Loaded....")

url="http://localhost:6333/dashboard"
collection_name="insurance_docs"

Qdrant=Qdrant.from_documents(
    documents=texts,
    embedding=embeddings,
    url=url,
    prefer_grpc=False #required for local qdrant instance
    ,collection_name=collection_name
)

print("Qdrant index created")
