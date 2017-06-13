#!/usr/bin/env python
"""
Script for concatenating largest number from provided list of integers

Date: 06/12/2017
Author: Anton Shestakov (anton.shestakov2@gmail.com)
"""

import argparse
import sys


def create_largest_number(input_data):
    """
    Performs concatenation of numbers in sequence into one and finds the largest possible combination

    :param input_data: sequence of integers
    :return: maximum combined number
    """

    max_len = len(str(max(input_data))) * 2

    return int(
        ''.join(
            sorted(
                (str(x) for x in input_data),
                key=lambda y: y*(max_len//len(y)),
                reverse=True
            )
        )
    )


def create_parser():
    parser = argparse.ArgumentParser(
        description='Concatenate largest number from provided list of integers'
    )

    parser.add_argument(
        'input', nargs='+', type=int,
        help='List of integers for concatenating'
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    sys.stdout.write(str(create_largest_number(args.input)))

if __name__ == '__main__':
    main()
