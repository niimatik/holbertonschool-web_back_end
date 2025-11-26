#!/usr/bin/env python3
"""Module that provides a function to measure the average execution
time of wait_n."""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the average time (in seconds) taken for wait_n to complete n
    executions with a given max_delay."""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n
