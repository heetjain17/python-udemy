import requests
from bs4 import BeautifulSoup
import csv

HN_URL = "https://news.ycombinator.com/"
CSV_FILE = "hn_top20.csv"

def fetch_top_post():
  try:
    response = requests.get(HN_URL, timeout=10)
    response.raise_for_status()

  except requests.RequestException as e:
    print(f"Failed to fetch page: \n{e}")
    return []
  
  soup = BeautifulSoup(response.text, "html.parser")
  post_links = soup.select("span.titleline > a")

  posts = []
  for link in post_links[:20]:
    title = link.text.strip()
    url = link.get("href").strip()  # type: ignore

    # print(f"\nTitle: {title}\nLink: {url}")
    posts.append({"title": title, "url": url})

  return posts

def save_to_csv(posts):
  with open(CSV_FILE, "w", newline="", encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["title", "url"])
    writer.writeheader()
    writer.writerows(posts)

  print("Saved top posts to CSV")

def main():
  posts = fetch_top_post()
  save_to_csv(posts)

if __name__ == "__main__":
  main()