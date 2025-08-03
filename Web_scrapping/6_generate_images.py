import requests
import os
import textwrap
from bs4 import BeautifulSoup # type: ignore
from PIL import Image, ImageDraw, ImageFont

BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_DIR = "quotes"

def fetch_quotes():
  response = requests.get(BASE_URL)
  soup = BeautifulSoup(response.text, 'html.parser')
  quotes = soup.select("div.quote")

  quote_data = []

  for q in quotes[:5]:
    text = q.find('span', class_="text").text.strip("“”") # type: ignore
    author = q.find("small", class_='author').text # type: ignore

    quote_data.append((text, author))

  return quote_data

def create_img(text, author, index):
  width, height = 800, 400
  bg_color = "#38b0c5"
  text_color = "#051A1D"

  img = Image.new('RGB', (width, height), bg_color)
  draw = ImageDraw.Draw(img)
  font = ImageFont.load_default()
  author_font = ImageFont.load_default()

  wrapped = textwrap.fill(text, width=60) 
  author_text = f"- {author}"

  y_text = 60
  draw.text((40, y_text), wrapped, font=font, fill=text_color)

  y_text += wrapped.count('\n') * 15 + 40
  draw.text((500, y_text), author_text, font=font, fill=text_color)

  if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

  filename = os.path.join(OUTPUT_DIR, f"quote_{index+1}.png")
  img.save(filename)
  print(f"saved: {filename}")

def main():
  quotes = fetch_quotes()
  for idx, (text, author) in enumerate(quotes):
    create_img(text, author, idx)

if __name__ == "__main__":
  main() 
  