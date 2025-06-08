import re
from typing import List

class TextCleaner:
    @staticmethod
    def clean_text(text: str) -> str:
        """Clean and normalize text."""
        # Remove special characters and extra whitespace
        text = re.sub(r'[^\w\s]', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    @staticmethod
    def preprocess_document(text: str) -> str:
        """Preprocess document text."""
        # Convert to lowercase
        text = text.lower()
        # Clean text
        text = TextCleaner.clean_text(text)
        return text