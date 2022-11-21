#!/usr/bin/env python3
"""Runs gendiff script."""
import argparse

from gendiff.data_loader import load_data
from gendiff.gendiff import generate_diff
from gendiff.formatters import stylish


def main():
    formatters = {
        'stylish': stylish
    }
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', help='set format of output', default='stylish',
    )
    args = parser.parse_args()
    data1 = load_data(args.first_file)
    data2 = load_data(args.second_file)
    formatter = formatters[args.format]
    diffs = generate_diff(data1, data2)
    dif_string = formatter(diffs)
    print(dif_string)


if __name__ == '__main__':
    main()
