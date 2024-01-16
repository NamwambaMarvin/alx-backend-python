#!/usr/bin/env python3
"""
    Asyncio Start
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        waits for an interval of a random
        number between 1 and max_value and
        returns the number
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
