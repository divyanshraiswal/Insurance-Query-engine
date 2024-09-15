from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from qdrant_client import QdrantClient

#load the model
model_name="BAAI/bge-base-en-v1.5"
model_kwargs={'device':'cpu'}
encode_kwargs={'normalize_embeddings':False} 

embeddings=HuggingFaceBgeEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

url="http://localhost:6333/dashboard"
collection_name="insurance_docs"

client=QdrantClient(
    url=url,
    prefer_grpc=False #required for local qdrant instance
)

print(client)
print("..............")

db=Qdrant(
    client=client,
    collection_name=collection_name,
    embeddings=embeddings
)
print(db)
print("..............")

query="What is the insurance policy for accidents?"

docs=db.similarity_search(query)
docs=db.similarity_search_with_score(query,k=5)

for i in docs:
    doc, score=i
    print({"Score":score,"Content":doc.page_content,"meta_data":doc.metadata})