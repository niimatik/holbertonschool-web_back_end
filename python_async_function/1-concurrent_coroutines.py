#!/usr/bin/env python3
"""
Module fournissant une fonction asynchrone qui lance
plusieurs délais aléatoires et renvoie leur ordre d’achèvement.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Retourne une liste des délais générés par
    plusieurs appels asynchrones à wait_random.
    """
    delays: List[float] = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for a in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
