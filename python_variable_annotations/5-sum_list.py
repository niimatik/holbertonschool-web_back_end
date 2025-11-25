#!/usr/bin/env python3
import typing
"""
Module fournissant une fonction qui calcule la somme des valeurs d'une liste.
"""

def sum_list(input_list: typing.List[float] ) -> float:
    """
    Retourne la somme de tous les éléments numériques d'une liste.
    """
    a: float = sum(input_list)
    return a
