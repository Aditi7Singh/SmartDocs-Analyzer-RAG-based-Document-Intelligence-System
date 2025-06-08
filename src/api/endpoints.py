from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from ..llm.rag_chain import RAGChain
from ..preprocessing.text_cleaner import TextCleaner
from ..preprocessing.document_splitter import DocumentSplitter

app = FastAPI()
rag_chain = RAGChain()
text_cleaner = TextCleaner()
doc_splitter = DocumentSplitter()

class Question(BaseModel):
    text: str

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")
    
    # Preprocess document
    cleaned_text = text_cleaner.preprocess_document(text)
    chunks = doc_splitter.split_document(cleaned_text)
    
    # Add to vector store
    rag_chain.vector_store.add_documents(chunks)
    return {"message": "Document processed successfully"}

@app.post("/ask")
async def ask_question(question: Question):
    answer = rag_chain.answer_question(question.text)
    return {"answer": answer}