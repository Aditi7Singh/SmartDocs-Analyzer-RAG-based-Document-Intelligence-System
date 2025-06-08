from typing import List, Dict
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from ..retriever.vector_store import VectorStore

class RAGChain:
    def __init__(self):
        self.vector_store = VectorStore()
        self.llm = OpenAI(temperature=0.7)
        self.prompt = PromptTemplate(
            input_variables=["context", "question"],
            template="""Use the following context to answer the question.
            Context: {context}
            Question: {question}
            Answer: """
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def answer_question(self, question: str) -> str:
        """Answer question using RAG approach."""
        # Retrieve relevant documents
        results = self.vector_store.search(question)
        context = "\n".join(results["documents"][0])
        
        # Generate answer
        response = self.chain.run(context=context, question=question)
        return response