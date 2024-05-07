#!/usr/bin/env python3
"""Async Comprehensions"""
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Takes no argument
    Collects 10 random numbers iterating over async_generator()
    Returns 10 random numbers"""
    result = []
    async for i in async_generator():
        result.append(i)

    return result
