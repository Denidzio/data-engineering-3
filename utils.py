import os
import glob
import json
import csv
from typing import Any

def get_json_recursively(json_file_dir: str):
    return glob.glob(os.path.join(json_file_dir, "**/*.json"), recursive=True)

def flatten_json(json: Any):
    def flatten(obj, name=''):
        flattened = {}

        if isinstance(obj, dict):
            for key, value in obj.items():
                flattened.update(flatten(value, f'{name}{key}_'))
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                flattened.update(flatten(item, f'{name}{i}_'))
        else:
            flattened[name[:-1]] = obj

        return flattened

    if isinstance(json, list):
        return [flatten(item) for item in json]
    else:
        return flatten(json)

def write_to_csv(data: any, filename: str):
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            writer.writerow(row)

def convert_json_into_csv(json_file_dir: str):
    with open(json_file_dir, 'r') as f:
        data = json.load(f)

    data = flatten_json(data)
    csv_filename = os.path.splitext(os.path.basename(json_file_dir))
    csv_filename = f'{csv_filename[0]}.csv'
    csv_path = os.path.join(os.path.dirname(json_file_dir), csv_filename)

    if isinstance(data, list):
        write_to_csv(data, csv_path)
    else:
        write_to_csv([data], csv_path)

