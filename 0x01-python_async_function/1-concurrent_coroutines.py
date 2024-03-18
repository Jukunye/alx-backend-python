#!/usr/bin/env python3
"""This module contains the function wait_n"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that calls wait_random n times
    and returns the list in ascending order.
    """
    return sorted([await wait_random(max_delay) for _ in range(n)])
