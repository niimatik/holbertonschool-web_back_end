#!/usr/bin/env python3
"""
Module fournissant une fonction qui calcule la somme des valeurs d'une liste.
"""

def sum_list(input_list: float) -> float:
    """
    Retourne la somme de tous les éléments numériques d'une liste.
    """
    a: float = 0.0
    for f in input_list:
        a = a + f
    return a
