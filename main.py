#!/usr/bin/env python
""" \
    Лабораторна робота №3
    Виконав студент 543 групи Лунгу Денис
"""

from utils import get_json_recursively, convert_json_into_csv

input_dir = 'data'


def main():
    json_files = get_json_recursively(input_dir)
    [convert_json_into_csv(json_file) for json_file in json_files]


if __name__ == "__main__":
    main()
