#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Takes no argument
    executes async_comprehension() four times in parallel using asyncio.gather
    Measures the total run time and returns it"""
    # tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    start = perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = perf_counter()
    elapsed = end - start
    return elapsed
