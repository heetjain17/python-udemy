import csv
from collections import defaultdict as diddy
import matplotlib.pyplot as plt 

FILENAME = "sample_data.csv"

def visualize_weather():
  dates = []
  temps = []
  conditions = diddy(int)

  with open(FILENAME, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
      try: 
        dates.append(row["Date"])
        temps.append(row["Temperature"])
        conditions[row["Condition"]] += 1
      except:
        continue
  if not dates or not temps or not conditions:
    print("No data available")
    return
  
  plt.figure(figsize=(10,7))
  plt.plot(dates, temps, marker='o')
  plt.title("Temperature overtime")
  plt.xlabel("Date")
  plt.ylabel("Temperature")
  plt.tight_layout()
  plt.grid(True)
  plt.show()

  plt.figure(figsize=(7,5))
  plt.bar(conditions.keys(), conditions.values(), color='skyblue')
  plt.xlabel("Condition")
  plt.ylabel("Days")
  plt.show()

visualize_weather()