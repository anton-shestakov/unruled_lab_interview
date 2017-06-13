#!/usr/bin/env python
"""
Script for finding anomaly element (even in odds or odd in evens) in sequence of numbers

Date: 06/12/2017
Author: Anton Shestakov (anton.shestakov2@gmail.com)
"""

import argparse
import sys


def find_anomaly_element(input_data):
    """
    Performs pattern finding (even/odds sequence) and searches for anomaly number

    :param input_data: sequence of numbers
    :return: number that is not "normal" compared to others
    """

    # 0 - odd numbers search for even
    # 1 - odd numbers even among first three
    # 2 - even numbers odd among first three
    # 3 - even numbers search for odd
    even_odd = 0 if sum(x % 2 for x in input_data[:3]) > 2 else 1

    return next(x for x in input_data if x % 2 == even_odd)


def create_parser():
    parser = argparse.ArgumentParser(
        description='Search for anomaly element in sequence of numbers'
    )

    parser.add_argument(
        'input', nargs='+', type=int,
        help='Sequence of numbers to search for anomaly element'
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    sys.stdout.write(str(find_anomaly_element(args.input)))

if __name__ == '__main__':
    main()
