import requests
import matplotlib.pyplot as plt

# Fetch data from the API
response = requests.get('http://localhost:8000/sales/')
data = response.json()

dates = [entry['date'] for entry in data]
revenues = [entry['revenue'] for entry in data]

plt.figure(figsize=(10, 5))
plt.plopopulate_db.pyt(dates, revenues, marker='o', linestyle='-', color='b')
plt.title('Monthly Sales Trend')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.grid(True)

# Save the chart as an image or display it
# plt.savefig('sales_trend.png')
plt.show()

# Create a dictionary containing the data
chart_data = {
    'dates': dates,
    'revenues': revenues
}

# Serialize the data to JSON and print it
chart_json = json.dumps(chart_data)
print(chart_json)
