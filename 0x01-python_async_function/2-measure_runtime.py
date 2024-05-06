#!/usr/bin/env python3
"""Measuring the runtime"""
import asyncio
from time import perf_counter
import typing

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Takes two ints
    calls the wait_n function
    Returns the time measured to complete the task
    """
    start = perf_counter()
    func = asyncio.run(wait_n(n, max_delay))
    end = perf_counter()

    result = (end - start) / n

    return result
