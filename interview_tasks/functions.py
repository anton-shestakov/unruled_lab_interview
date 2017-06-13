#!/usr/bin/env python
"""
Functions for Python interview. Usage: import and call.

Date: 06/12/2017
Author: Anton Shestakov (anton.shestakov2@gmail.com)
"""


def list_names(input_data):
    """
    Performs concatenation of names contained in sequence of dictionaries with all separators ',' except last '&'

    :param input_data: sequence of dictionaries containing names to concatenate
    :return: concatenated string
    """

    n = len(input_data)

    if n > 1:
        start = ', '.join(x['name'] for x in input_data[:-1])
        end = input_data[-1]['name']
        return '%(start)s & %(end)s' % locals()
    elif n > 0:
        return input_data[0]['name']


def count_produced(recipe, available):
    """
    Counts number of servings that can be prepared using recipe and available ingredients

    :param recipe: dictionary containing quantity of ingredients for preparing food
    :param available: dictionary containing quantity of available ingredients for preparation
    :return: integer
    """

    try:
        return min(available[x]//recipe[x] for x in recipe)
    except KeyError:  # ingredient not available so can't produce product
        return 0
