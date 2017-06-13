#!/usr/bin/env python
"""
Script for converting input string to camelCase (case of first word is preserved)

Date: 06/12/2017
Author: Anton Shestakov (anton.shestakov2@gmail.com)
"""

import argparse
import sys


def convert_to_camel_case(input_data):
    """
    Performs conversion of string to camel case with parts separated by '-' or '_'

    :param input_data: string to convert
    :return: converted string
    """

    import re

    t = re.split(r'_|-', input_data)
    title = str.title

    if t:
        return t[0] + ''.join(title(x) for x in t[1:])


def create_parser():
    parser = argparse.ArgumentParser(
        description='Sort provided list of words and numbers'
    )

    parser.add_argument(
        'input', type=str,
        help='''String to be converted (separators: '-', '_')'''
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    sys.stdout.write(convert_to_camel_case(args.input))

if __name__ == '__main__':
    main()
