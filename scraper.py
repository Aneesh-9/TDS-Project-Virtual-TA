import requests
import json
import time

BASE_URL = "https://discourse.onlinedegree.iitm.ac.in"
CATEGORY_ID = 29  # Replace with correct category ID for TDS if needed
MAX_PAGES = 10

all_posts = []

for page in range(1, MAX_PAGES + 1):
    print(f"Scraping page {page}...")
    url = f"{BASE_URL}/c/tools-in-data-science/{CATEGORY_ID}.json?page={page}"
    try:
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        for topic in data.get("topic_list", {}).get("topics", []):
            topic_id = topic["id"]
            topic_url = f"{BASE_URL}/t/{topic_id}.json"
            topic_res = requests.get(topic_url)
            topic_data = topic_res.json()
            all_posts.append({
                "id": topic_id,
                "title": topic["title"],
                "url": f"{BASE_URL}/t/{topic_id}",
                "posts": [post["cooked"] for post in topic_data["post_stream"]["posts"]]
            })
            time.sleep(0.5)
    except Exception as e:
        print("Error scraping:", e)

with open("data/discourse_posts.json", "w", encoding="utf-8") as f:
    json.dump(all_posts, f, indent=2)

print(f"✅ Done. Scraped {len(all_posts)} topics.")