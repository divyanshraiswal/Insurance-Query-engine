#1. Setting Up Qdrant with Docker
To run Qdrant in a Docker container, follow these steps:

Pull the Qdrant Docker Image:

```bash
docker pull qdrant/qdrant
```
Run Qdrant Container:

```bash
docker run -p 6333:6333 qdrant/qdrant
```

#2. Installing Required Libraries
Before running any scripts, ensure that all required Python libraries are installed:

```bash
pip install -r requirements.txt
```
#3. Usage of ingest.py
The ingest.py script processes the PDF document, generates vector embeddings from the text, and stores these embeddings in the Qdrant vector database.

How It Works:
Load the PDF: Reads the content of the specified PDF file.
Split the Text: Divides the text into manageable chunks for generating embeddings. Each chunk may slightly overlap to preserve context.
Generate Embeddings: Transforms each text chunk into a vector embedding using a pre-trained model.
Store in Qdrant: Stores the generated embeddings and their corresponding text in the Qdrant vector database.
Usage:
Run the following command to process and ingest data into Qdrant:

```bash
python ingest.py 
```
#4. Usage of app.py
The app.py script is used to query the Qdrant vector database to retrieve documents based on a user-provided query.

How It Works:
Embedding the Query: Converts the input query into a vector embedding using the same model used for document embeddings.
Similarity Search: Compares the query embedding with the stored embeddings in Qdrant to find the most similar documents.
Returning Results: Retrieves and displays the top matching documents based on similarity scores.
Usage:
Run the following command to start querying:

```bash
      python app.py
```
Make sure the Qdrant container is running and the data has been ingested using the ingest.py script.

