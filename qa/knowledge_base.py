import json
import os
from sentence_transformers import SentenceTransformer, util

# Load a pretrained transformer model for semantic similarity
model = SentenceTransformer("all-MiniLM-L6-v2")

# These hold our content and its vector representation
knowledge_data = []
knowledge_embeddings = None

# Load and embed posts
def load_knowledge_base():
    global knowledge_data, knowledge_embeddings
    filepath = os.path.join("data", "discourse_posts.json")

    if not os.path.exists(filepath):
        raise FileNotFoundError("data/discourse_posts.json not found. Run the scraper first!")

    with open(filepath, "r") as f:
        knowledge_data = json.load(f)

    texts = [entry["title"] + " — " + entry["url"] for entry in knowledge_data]
    knowledge_embeddings = model.encode(texts, convert_to_tensor=True)

    print(f"✅ Loaded and embedded {len(texts)} Discourse posts.")

# Given a student question, return top matching Discourse links
def get_relevant_posts(question, top_k=3):
    question_embedding = model.encode(question, convert_to_tensor=True)
    hits = util.semantic_search(question_embedding, knowledge_embeddings, top_k=top_k)[0]

    results = []
    for hit in hits:
        entry = knowledge_data[hit["corpus_id"]]
        results.append({
            "url": entry["url"],
            "text": entry["title"]
        })

    return results