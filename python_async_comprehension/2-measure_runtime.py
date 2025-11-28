#!/usr/bin/env python3
"""Module that measures the total runtime of running async_comprehension
four times in parallel."""

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime of executing async_comprehension
    4 times in parallel."""
    start = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.perf_counter()
    delay = end - start
    return delay
