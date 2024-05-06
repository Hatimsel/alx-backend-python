#!/usr/bin/env python3
"""Executing multiple coroutines at the same time with async"""
import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Takes two ints
    Calls task_wait_random n times
    Returns a list of floats"""

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    return sorted(delays)
