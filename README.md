# Insurance-Handbook-Query-System

1. Setting Up Qdrant with Docker
You start by running Qdrant, a vector database, inside a Docker container. Qdrant provides the infrastructure for storing and retrieving vector embeddings. Running it in Docker ensures that it’s isolated and can be easily accessed through its API on a specific port (e.g., 6333).

2. Ingesting Data (with ingest.py)
The ingest.py script processes the PDF document you want to store in the vector database. Here's what happens:

Loading the PDF: The script reads the contents of a PDF file and converts it into text.
Splitting the Text: Since embeddings are usually generated on smaller pieces of text, the script divides the document into manageable chunks of a few hundred or thousand characters. This also includes some overlap between chunks to preserve context.
Generating Embeddings: Each text chunk is transformed into a numerical vector (embedding) using a pre-trained machine learning model. These embeddings represent the semantic meaning of the text and allow for similarity searches.
Storing in Qdrant: The embeddings, along with the original text, are sent to the Qdrant vector database. They are indexed, meaning they are stored in a way that allows for efficient retrieval based on similarity searches.
3. Querying the Database (with app.py)
Once the embeddings are indexed in Qdrant, you can query the database to find documents similar to a given input. The app.py script likely handles this:

Embedding the Query: A new input, such as a search query or a question, is converted into an embedding (just like the document chunks were).
Similarity Search: The query embedding is compared with the stored embeddings in Qdrant to find the most similar ones. This allows you to retrieve relevant documents that match the meaning of the query.
Returning Results: Based on the similarity scores, the top matching documents are returned, providing answers or insights relevant to the input query.
4. Workflow Overview
You start Qdrant in Docker to manage document embeddings.
The ingest.py script processes and stores your documents (from the PDF) as embeddings in Qdrant.
The app.py script allows you to search Qdrant by embedding a query and retrieving the most similar document embeddings stored in the database.


