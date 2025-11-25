#!/usr/bin/env python3
"""
Module fournissant une fonction qui calcule la somme des valeurs d'une liste.
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    Retourne la somme de tous les éléments numériques d'une liste.
    """
    a: float = sum(mxd_lst)
    return a
