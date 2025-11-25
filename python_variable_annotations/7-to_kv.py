#!/usr/bin/env python3
"""
Module fournissant une fonction qui transforme
une clé et une valeur numérique en tuple.
"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    Retourne un tuple dont la première valeur
    est la chaîne k et la seconde est basée sur v.
    """
    a: tuple = (k, v ** 2)
    return a
