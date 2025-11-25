#!/usr/bin/env python3
"""
Module fournissant une fonction asynchrone qui attend un délai aléatoire avant de le renvoyer.
"""


import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    """
    Retourne un délai aléatoire après l'avoir attendu de manière asynchrone.
    """
    timer = random.uniform(0, max_delay)
    await asyncio.sleep(timer)
    return timer
