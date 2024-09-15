# Insurance-Handbook-Query-System

## 1. Setting Up Qdrant with Docker

To run Qdrant in a Docker container, follow these steps:

1. **Pull the Qdrant Docker Image:**
      docker pull qdrant/qdrant

2.**Run Qdrant Container:**

   docker run -p 6333:6333 qdrant/qdrant


## Running the Script
Install Required Libraries: pip install -r requirements.txt

## 2.Usage of ingest.py
The ingest.py script is designed to process a PDF document, generate vector embeddings from its text, and store these embeddings in the Qdrant vector database. This process involves extracting text from the PDF, chunking it into manageable parts, generating embeddings for each chunk, and then storing these embeddings in Qdrant.

# How It Works
Load the PDF: The script reads the contents of the specified PDF file.
Split the Text: The text is divided into smaller chunks to create embeddings efficiently. Each chunk may overlap slightly to preserve context.
Generate Embeddings: Each chunk of text is transformed into a vector embedding using a pre-trained model.
Store in Qdrant: The generated embeddings, along with the original text, are stored in the Qdrant database for later retrieval.

## 2/ Usage of app.py
The app.py script is designed to query the Qdrant vector database and retrieve documents similar to a given input query. It takes a user-provided query, converts it into an embedding, and searches the database for the most similar embeddings. The results are then returned to the user based on similarity scores.

# How It Works
Embedding the Query: The script converts the input query into a vector embedding using the same model used for document embeddings.
Similarity Search: The query embedding is compared against the stored embeddings in Qdrant to find the most similar ones.
Returning Results: The script retrieves and displays the top matching documents based on similarity scores.
Prerequisites
Before running app.py, ensure that you have:

Installed the required Python libraries (see requirements.txt).
Ingested data into Qdrant using the ingest.py script.
