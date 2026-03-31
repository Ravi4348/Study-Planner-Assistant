import json
from sentence_transformers import SentenceTransformer
import faiss

def load_data(path="data/syllabus.txt"):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = text.split("\n\n")  # simple chunking by paragraph
    return chunks

def build_index():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    docs = load_data()

    embeddings = model.encode(docs)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    faiss.write_index(index, "rag.index")

    with open("docs.json", "w") as f:
        json.dump(docs, f)

    print("Index built successfully!")

if __name__ == "__main__":
    build_index()
