#!/usr/bin/env python3
"""
Module fournissant une fonction qui crée un multiplicateur basé sur une valeur flottante.
"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    Retourne une fonction qui multiplie un nombre flottant par multiplier.
    """
    def multiplied(i: float) -> float:
        return i * multiplier
    return multiplied
