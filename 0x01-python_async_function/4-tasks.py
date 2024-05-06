#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a
new function task_wait_n. The code is nearly
identical to wait_n except task_wait_random
is being called.
"""

import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    this module Import wait_random from the
    previous python file that you’ve written
    and write an async routine called wait_n
    that takes in 2 int arguments (in this order):
    n and max_delay. You will spawn wait_random
    n times with the specified max_delay
    """

    tasks = []
    results = []
    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for j in asyncio.as_completed(tasks):
        result = await j
        results.append(result)
    return results
