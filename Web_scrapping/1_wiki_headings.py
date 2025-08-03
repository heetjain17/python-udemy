import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

def get_h2_headers(url):
  try:
    res = requests.get(url, timeout=10)
    res.raise_for_status()
  except requests.RequestException as e:
    print(f"Failed to fetch page: \n{e}")
  
  soup = BeautifulSoup(res.text, "html.parser")
  h2_tags = soup.find_all("h2")
  # print(h2_tags)
  headers = []
  for tag in h2_tags:
    header_text = tag.get_text(strip=True)
    if header_text and header_text.lower() != "contents":
      headers.append(header_text)
  
  for i, h in enumerate(headers, 1):
    if i == 11:
      break
    print(f"{i}. {h}")


def main():
  get_h2_headers(URL)
  
if __name__ == "__main__":
  main()