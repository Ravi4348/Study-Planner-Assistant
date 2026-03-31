import faiss
import json
from sentence_transformers import SentenceTransformer

class RAGEngine:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.read_index("rag.index")
        self.docs = json.load(open("docs.json", "r", encoding="utf-8"))

    def retrieve(self, query, k=3):
        emb = self.model.encode([query])
        D, I = self.index.search(emb, k)
        return [self.docs[idx] for idx in I[0]]

    def generate_plan(self, date, hours, subject):
        retrieved = self.retrieve(subject)

        plan = f"""
        Study Plan for {date}

        Subject: {subject}
        Total Study Hours: {hours}

        Recommended Topics from RAG:
        1. {retrieved[0][:200]}...
        2. {retrieved[1][:200]}...
        3. {retrieved[2][:200]}...

        Suggested Time Allocation:
        - 40%: Core Concepts
        - 30%: Practice Questions
        - 20%: Revision
        - 10%: Mock Tests

        Personalized Tips:
        • Start with the highest-weightage topics.
        • Do spaced repetition for weak areas.
        """

        return plan
