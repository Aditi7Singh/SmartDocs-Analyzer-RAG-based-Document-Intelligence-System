from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP

class DocumentSplitter:
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            length_function=len,
        )

    def split_document(self, text: str) -> List[str]:
        """Split document into chunks."""
        return self.text_splitter.split_text(text)