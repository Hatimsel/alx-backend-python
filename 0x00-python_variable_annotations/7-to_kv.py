#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""
from typing import Union, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a string and an int or float
    Returns a tuple"""
    return (k, float(v * v))
