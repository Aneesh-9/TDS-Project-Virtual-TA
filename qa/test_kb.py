from knowledge_base import load_knowledge_base, get_relevant_posts

# Step 1: Load all embeddings from Discourse
load_knowledge_base()

# Step 2: Try a test question
question = "Which GPT model should I use for GA5 question 8?"
results = get_relevant_posts(question)

# Step 3: Print results
print("\nTop matching posts:\n")
for r in results:
    print(f"- {r['text']} \n  {r['url']}\n")