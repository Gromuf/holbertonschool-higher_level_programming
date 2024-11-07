#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)
JSON_FILE_PATH = 'products.json'
CSV_FILE_PATH = 'products.csv'


def read_json_data():
    try:
        with open(JSON_FILE_PATH, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def read_csv_data():
    try:
        products = []
        with open(CSV_FILE_PATH, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
            return products
    except (FileNotFoundError, csv.Error):
        return None


@app.route('/products')
def display_products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', type=int)

    if source == 'json':
        products = read_json_data()
    elif source == 'csv':
        products = read_csv_data()
    else:
        return render_template(
            "product_display.html",
            error="Wrong source parameter value. Choose 'json' or 'csv'."
            )
    if products is None:
        return render_template(
            "product_display.html", error="Error reading data from the file."
        )

    if product_id:
        products = [
            product for product in products if product['id'] == product_id
            ]
        if not products:
            return render_template(
                "product_display.html", error="Product not found."
            )

    return render_template(
        "product_display.html", products=products
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
