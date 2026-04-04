from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route("/products")
def home():
    source = request.args.get("source")
    id = request.args.get("id")

    if not source in ["json", "csv"]:
        return render_template("product_display.html", error="Wrong source")

    if source == "json":
        with open("products.json", "r") as f:
            products = json.load(f)

    return render_template("product_display.html", products=products)
