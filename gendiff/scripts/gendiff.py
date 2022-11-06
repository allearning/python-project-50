#!/usr/bin/env python3
"""Runs gendiff script."""
import argparse

from gendiff.data_loader import load_flat_data
from gendiff.gendiff import compare_dicts


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    data1 = load_flat_data(args.first_file)
    data2 = load_flat_data(args.second_file)
    diffs = compare_dicts(data1, data2)
    print(diffs)


if __name__ == '__main__':
    main()
