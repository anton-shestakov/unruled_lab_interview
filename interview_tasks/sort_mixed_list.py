#!/usr/bin/env python
"""
Script for sorting provided list of words and numbers

Date: 06/12/2017
Author: Anton Shestakov (anton.shestakov2@gmail.com)
"""

import argparse
import sys


def sort_mixed_list(input_data):
    """
    Performs sorting of input list by following rules:
    1. Treats numbers and words separately
    2. Preserves original position of numbers and words but sorts them within partitions

    :param input_data: list that needs to be sorted
    :return: sorted list
    """

    input_flags = (isinstance(x, int) for x in input_data)
    numbers_sorted = iter(sorted(x for x in input_data if isinstance(x, int)))
    words_sorted = iter(sorted(x for x in input_data if not isinstance(x, int)))

    return [next(numbers_sorted) if flag else next(words_sorted) for flag in input_flags]


def create_parser():
    parser = argparse.ArgumentParser(
        description='Sort provided list of words and numbers'
    )

    def int_or_str(v):
        """conversion function for arg parsing"""

        try:
            return int(v)
        except ValueError:
            return v

    parser.add_argument(
        'input', nargs='+', type=int_or_str,
        help='Words and numbers to sort'
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    sys.stdout.write(str(sort_mixed_list(args.input)))

if __name__ == '__main__':
    main()
