#!/usr/bin/env python3
"""Complex types - list of floats"""
from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a list of floats
    Returns their sum"""
    return reduce(lambda x, y: x + y, input_list)
