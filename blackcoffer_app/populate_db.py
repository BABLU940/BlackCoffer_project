import csv
from .models import Sale
from decimal import Decimal

with open('sales_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Sale.objects.create(
            date=row['Date'],
            revenue=Decimal(row['Revenue'])
        )
