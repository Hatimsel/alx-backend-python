#!/usr/bin/env python3
""" Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a multiplier and returns a callable"""
    def multiplier_func(value: float) -> float:
        return value * multiplier
    return multiplier_func
