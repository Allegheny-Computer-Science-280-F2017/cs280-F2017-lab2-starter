"""Test suite for the duplicates.py module"""

import pytest
import generator


def test_generate_lists_from_three_items():
    """ Generate a list of lists from three items """
    list = [1, 2, 3]
    list_of_lists = generator.generate(list)
    assert len(list) == 3
    assert len(list_of_lists) == 4
    assert (list in list_of_lists) is True


def test_generate_lists_from_four_items():
    """ Generate a list of lists from four items """
    list = [1, 2, 3, 4]
    list_of_lists = generator.generate(list)
    assert len(list) == 4
    assert len(list_of_lists) == 7
    assert (list in list_of_lists) is True
