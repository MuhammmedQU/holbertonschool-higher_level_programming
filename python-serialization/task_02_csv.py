#!/usr/bin/python3
"""work code with Json."""

import csv
import json


def convert_csv_to_json(filename):
    try:
        data = []
        with open(filename, "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)

        with open("data.json", "w") as file:
            json.dump(data, file)
        return True
    except Exception:
        return False
