#!/usr/bin/env python3
"""Runs gendiff script."""
import argparse

from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', help='set format of output', default='stylish',
    )
    args = parser.parse_args()
    file1 = args.first_file
    file2 = args.second_file
    formatter = args.format
    diffs = generate_diff(file1, file2, formatter)
    print(diffs)


if __name__ == '__main__':
    main()
