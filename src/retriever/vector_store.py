from typing import List, Dict
from chromadb import Client
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL

class VectorStore:
    def __init__(self):
        self.client = Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory="data/embeddings"
        ))
        self.model = SentenceTransformer(EMBEDDING_MODEL)
        self.collection = self.client.create_collection("documents")

    def add_documents(self, texts: List[str], metadata: List[Dict] = None):
        """Add documents to the vector store."""
        embeddings = self.model.encode(texts).tolist()
        self.collection.add(
            embeddings=embeddings,
            documents=texts,\            metadatas=metadata if metadata else [{}] * len(texts),
            ids=[str(i) for i in range(len(texts))]
        )

    def search(self, query: str, k: int = 3) -> List[Dict]:
        """Search for similar documents."""
        query_embedding = self.model.encode(query).tolist()
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )
        return results