📄 SmartDocs Analyzer
SmartDocs Analyzer is a sophisticated RAG (Retrieval-Augmented Generation) based document analysis system that combines LLM capabilities with custom NLP processing for intelligent document understanding and Q&A.

🚀 Features
✅ Advanced document preprocessing and text cleaning

✅ Intelligent document chunking for optimal retrieval

✅ Custom embedding using sentence-transformers

✅ ChromaDB for vector store and similarity search

✅ LLM-powered contextual question answering

✅ RESTful API built with FastAPI

📁 Project Structure
bash
Copy
Edit
.
├── config.py                 # Configuration settings
├── main.py                  # Entry point for FastAPI app
├── requirements.txt         # Python dependencies
└── src/
    ├── api/
    │   └── endpoints.py     # FastAPI endpoints
    ├── llm/
    │   └── rag_chain.py     # RAG implementation
    ├── preprocessing/
    │   ├── document_splitter.py  # Chunking logic
    │   └── text_cleaner.py       # Text cleaning utilities
    └── retriever/
        └── vector_store.py  # ChromaDB integration
🔧 Installation
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/Aditi7Singh/smartdocs-analyzer.git
cd smartdocs-analyzer
2. Set up a virtual environment (recommended)
bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
3. Install the dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set your environment variables
bash
Copy
Edit
# Replace with your actual OpenAI API key
export OPENAI_API_KEY=your_api_key_here
▶️ Usage
Start the FastAPI server
bash
Copy
Edit
python main.py
Visit the interactive docs at: http://localhost:8000/docs

📡 API Endpoints
POST /upload
Upload documents for analysis.

Accepts: .pdf, .txt, .docx

Returns: Document ID for future queries

POST /ask
Ask questions based on a previously uploaded document.

Parameters:

document_id: ID of the document

question: User's query

Returns: AI-generated answer with contextual reference

⚙️ Technical Details
🧹 Document Processing Pipeline
Custom text normalization

Chunking based on semantic boundaries

Metadata tagging for retrieval context

🔍 Vector Store Integration
ChromaDB for fast similarity search

Sentence-transformers for embedding generation

🤖 RAG-Based Q&A
Context-aware retrieval and answer generation

Prompt engineering for higher quality responses

🛠️ Built With
Python 3.8+

LangChain

FastAPI

ChromaDB

Sentence-Transformers

OpenAI API

🧑‍💻 Contributing
Contributions are welcome!

Fork the project

Create your feature branch: git checkout -b feature/my-feature

Commit your changes: git commit -m 'Add my feature'

Push to the branch: git push origin feature/my-feature

Open a pull request

👩‍🔬 Maintainer
Aditi Singh – Project Lead & Main Developer

📄 License
This project is licensed under the MIT License.

java
Copy
Edit
MIT License

Copyright (c) 2024 Aditi Singh
