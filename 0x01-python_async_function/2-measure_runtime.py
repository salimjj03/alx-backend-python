#!/usr/bin/env python3
"""
From the previous file, import wait_n into 2-measure_runtime.py.
Create a measure_time function with integers n and max_delay
as arguments that measures the total execution time for wait_n
(n, max_delay), andreturns total_time / n. Your function should
return a float.
Use the time module to measure an approximate elapsed time.
"""

wait_n = __import__("1-concurrent_coroutines").wait_n
import asyncio
import time
from typing import List
from random import randint


def measure_time(n: int, max_delay: int) -> float:
    """
    From the previous file, import wait_n into 2-measure_runtime.py.
    Create a measure_time function with integers n and max_delay
    as arguments that measures the total execution time for wait_n
    (n, max_delay), andreturns total_time / n. Your function should
    return a float.
    Use the time module to measure an approximate elapsed time.
    """

    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    average = (end - start) / n

    return average
