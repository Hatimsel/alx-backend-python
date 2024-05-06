#!/usr/bin/env python3
"""The basics of async"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Takes an int
    waits a random delay between 0, and the int passed
    Returns the time waited"""
    time_waited = random.uniform(0, max_delay)
    time_waited = await asyncio.sleep(time_waited, result=time_waited)

    return time_waited
