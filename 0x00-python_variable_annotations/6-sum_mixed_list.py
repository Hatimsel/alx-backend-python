#!/usr/bin/env python3
"""Complex types - mixed list"""
from functools import reduce
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    """Takes a mixed list
    Returns their sum"""
    return reduce(lambda x, y: x + y, mxd_list)
