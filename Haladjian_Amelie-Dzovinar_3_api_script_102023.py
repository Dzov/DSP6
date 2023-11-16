import requests
import csv

url = "https://edamam-food-and-grocery-database.p.rapidapi.com/api/food-database/v2/parser"

querystring = {"ingr": "champagne"}

headers = {
    "X-RapidAPI-Key": "YOUR-API-KEY",
    "X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

products = []

for item in response.json()['hints']:
    if (len(products) < 10):
        product = {
            'foodId': item['food']['foodId'] if 'foodId' in item['food'] else None,
            'label': item['food']['label'] if 'label' in item['food'] else None,
            'category': item['food']['category'] if 'category' in item['food'] else None,
            'foodContentsLabel': item['food']['foodContentsLabel'] if 'foodContentsLabel' in item['food'] else None,
            'image': item['food']['image'] if 'image' in item['food'] else None,
        }
        products.append(product)


csv_file_path = 'champagne_products.csv'
field_names = ['foodId', 'label', 'category', 'foodContentsLabel', 'image']
print(products)
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()

    for row in products:
        writer.writerow(row)
