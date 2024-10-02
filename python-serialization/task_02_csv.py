#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        with open(
            csv_filename, mode='r', newline='', encoding='utf-8'
        ) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except FileNotFoundError:
        print("Error: The file {} was not found.".format(csv_filename))
        return False
    except Exception as err:
        print("An error occurred: {}".format(err))
        return False
