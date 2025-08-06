import requests
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
# import schedule
import  time

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
  'vs_currency': 'usd',
  'order': 'market_cap_desc',
  'per_page': 10,
  'page': 1,
  'sparkline': False
}

CSV_FILE = 'crypto_prices.csv'

def fetch_data():
  response = requests.get(API_URL, PARAMS)
  return response.json()

def save_to_csv(data):
  file_exists = os.path.isfile(CSV_FILE)

  with open(CSV_FILE, 'a', newline='') as f:
    writer = csv.writer(f)
    if not file_exists:
      writer.writerow(['timestamps', 'coin', 'price'])

    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    for coin in data: 
      writer.writerow([timestamp, coin["id"], coin["current_price"]])
    print("✅ Data saved to csv")

def plot_graph(coin_id):
  times = []
  prices = []

  with open(CSV_FILE, newline='')as f:
    reader = csv.DictReader(f)
    for row in reader:
      if row['coin'] == coin_id: 
        times.append(row['timestamps'])
        prices.append(float(row['price']))

  if not times:
    print(f"No data found for {coin_id}")
    return
  
  plt.figure(figsize=(10, 5))
  plt.plot(times, prices, marker='o')
  plt.tight_layout()
  plt.grid()
  plt.show()

def main():
  # print("Ferching live crypto data...")
  # crypto_data = fetch_data()
  # save_to_csv(crypto_data)

  # for coin in crypto_data:
  #   print(f"{coin['id']} - ${coin['current_price']}")
  # print("-"*30)

  choice = input("Enter the coin name to get graph: ").strip().lower()
  if choice:
    plot_graph(choice)

main()
# def job():
#   print("Fetching data every 10 seconds...")
#   crypto_data = fetch_data()
#   save_to_csv(crypto_data)


# schedule.every(20).seconds.do(job)

# while True:
#   schedule.run_pending()
#   time.sleep(1)