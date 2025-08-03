import os
import csv
from datetime import datetime
import requests
from collections import Counter

FILENAME = "weather_logs.csv"
API_KEY = "f41c9290c724cc66f0deb81f815538c7"

if not os.path.exists(FILENAME):
  with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "City", "Temperature", "Condition"])

def log_weather():
  city = input("Enter your city name: ").strip().lower()
  date = datetime.now().strftime("%Y-%m-%d")
  
  with open(FILENAME, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
      if row["Date"] == date and row["City"].lower() == city:
        print("-"*40)
        print("Entry for this city and date exists you saved an API call")
        print(f"Logged: {row["Temperature"]} {row["Condition"]} in {row["City"]} on {row["Date"]}")
        print("-"*40)
        return
  
  try:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
      print(f"API Error {data.get('message')}")
      return
    
    temp = data["main"]["temp"]
    condition = data["weather"][0]["main"]

    with open(FILENAME, 'a', newline='', encoding='utf-8') as f:
      writer = csv.writer(f)
      writer.writerow([date, city.title(), temp, condition])

    
    print("-"*40)
    print(f"Logged: {temp} {condition} in {city.title()} on {date}")
    print("-"*40)

  except Exception as e:
    print("Failed to make API call")

def view_logs():
  with open(FILENAME, 'r', encoding='utf-8') as f:
    reader = list(csv.reader(f))
    if len(reader) <= 1:
      print("No Entries")
      return
    print("-"*40)
    for index, row in enumerate(reader[1:]):
      print(f"{index+1}. {row[0]} : {row[1]} : {row[2]} : {row[3]}")
    print("-"*40)

def view_stats():
  with open(FILENAME, 'r', encoding='utf-8') as f:
    reader = list(csv.reader(f))
    if len(reader) <= 1:
      print("No Entries")
      return
    temperature_list = []
    condition_list = []
    for row in reader[1:]:
      temperature_list.append(float(row[2]))
      condition_list.append(row[3])

    most_common_condition = Counter(condition_list).most_common(1)
    print("-"*40)
    print("Maximum temperature:", max(temperature_list), "K")
    print("Minimum temperature:", min(temperature_list), "K")
    print("Average temperature:", sum(temperature_list) / len(temperature_list), "K")
    print("Most frequent condition:", most_common_condition[0][0])
    print("-"*40)

def main():
  while True: 
    print("Real time weather logger")

    print("1. Get weather log")
    print("2. View all weather logs")
    print("3. Stats for geeks")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    match choice:
      case "1":
        log_weather()
      case "2":
        view_logs()
      case "3":
        view_stats()
      case "4":
        break 
      case _: 
        print("Invalid Choice")

if __name__ == "__main__":
  main()