#!/usr/bin/env python3
"""Executing multiple coroutines at the same time with async"""
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Takes two ints
    Calls wait_random n times
    Returns a list of floats"""

    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    return sorted(delays)
