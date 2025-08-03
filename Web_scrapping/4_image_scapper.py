import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

BASE_URL = "https://books.toscrape.com/"
IMAGE_DIR = "images"

def sanitize_filename(title):
  return re.sub(r'[^\w\-_. ]', '', title).replace(" ", "_")

def download_img(img_url, filename):
  try:
    res = requests.get(img_url, stream=True, timeout=10)
    res.raise_for_status()
    with open(filename, 'wb')as f:
      for chunk in res.iter_content(8192):
        f.write(chunk)
  except Exception as e:
    print(f"Failed to download {filename} -\n{e}")

def scrape_and_download_images():
  res = requests.get(BASE_URL)
  soup = BeautifulSoup(res.text, "html.parser")
  books = soup.select("article.product_pod")[:10]
  if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

  for book in books:
    title = book.h3.a['title'] # type: ignore
    rel_img = book.find("img")["src"] # type: ignore
    img_url = urljoin(BASE_URL, rel_img) # type: ignore
    print(f"url: {img_url}")

    filename = sanitize_filename(title) + ".jpg"
    filepath = os.path.join(IMAGE_DIR, filename)
    print(f"filepath - {filepath}")

    print(f"Downloading: {title}")
    download_img(img_url, filepath)
  print("All 10 books images downloaded /-")

if __name__ == "__main__":
  scrape_and_download_images()