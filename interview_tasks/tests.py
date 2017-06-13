#!/usr/bin/env python
"""
Module for testing interview scripts and functions. Usage: invoke python script

Date: 06/12/2017
Author: Anton Shestakov (anton.shestakov2@gmail.com)
"""

import unittest
from functions import list_names, count_produced
from sort_mixed_list import create_parser as parser_mixed_list, sort_mixed_list
from find_anomaly_element import create_parser as parser_anomaly_element, find_anomaly_element
from create_largest_number import create_parser as parser_largest_number, create_largest_number
from convert_to_camel_case import create_parser as parser_camel_case, convert_to_camel_case


class TestSortMixedList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        parser = parser_mixed_list()
        cls.parser = parser

    def test_find_anomaly_element(self):
        input_args = self.parser.parse_args(["yellow", "white", "2", "5", "green", "red", "6", "1"])

        self.assertEqual(sort_mixed_list(input_args.input), ["green", "red", 1, 2, "white", "yellow", 5, 6])


class TestFindAnomalyElement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        parser = parser_anomaly_element()
        cls.parser = parser

    def test_find_anomaly_element(self):
        input_args = self.parser.parse_args(["0", "8", "2", "50", "13", "6", "34"])

        self.assertEqual(find_anomaly_element(input_args.input), 13)


class TestCreateLargestNumber(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        parser = parser_largest_number()
        cls.parser = parser

    def test_create_largest_number(self):

        input_args = self.parser.parse_args(["70", "8", "20", "1", "13"])

        self.assertEqual(create_largest_number(input_args.input), 87020131)


class TestConvertToCamelCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        parser = parser_camel_case()
        cls.parser = parser

    def test_convert_to_camel_case_conversion(self):

        input_args = [
            "the_phantom_menace",
            "The-Phantom-Menace",
            "the_test"
        ]

        expected_results = [
            "thePhantomMenace",
            "ThePhantomMenace",
            "theTest"
        ]

        for index, arg in enumerate(input_args):
            args = self.parser.parse_args([arg])
            result = convert_to_camel_case(args.input)
            self.assertEqual(result, expected_results[index])

    def test_convert_to_camel_case_no_conversion(self):
        input_args = [
            "the",
            "theTest"
        ]

        expected_results = [
            "the",
            "theTest"
        ]

        for index, arg in enumerate(input_args):
            args = self.parser.parse_args([arg])
            result = convert_to_camel_case(args.input)
            self.assertEqual(result, expected_results[index])


class TestFunctions(unittest.TestCase):

    def test_list_names(self):

        input_args = [
            [{'name': 'John'}, {'name': 'Jack'}, {'name': 'Joe'}],
            [{'name': 'John'}, {'name': 'Jack'}],
            [{'name': 'John'}]
        ]

        expected_results = [
            'John, Jack & Joe',
            'John & Jack',
            'John'
        ]

        for index, args in enumerate(input_args):
            self.assertEqual(list_names(args), expected_results[index])

    def test_count_produced(self):
        recipe = {"flour": 500, "sugar": 200, "eggs": 1}
        available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
        self.assertEqual(count_produced(recipe, available), 2)


if __name__ == '__main__':
    unittest.main()
