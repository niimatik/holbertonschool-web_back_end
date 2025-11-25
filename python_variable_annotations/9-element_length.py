#!/usr/bin/env python3
"""
Module fournissant une fonction qui associe
chaque élément d’un iterable à sa longueur.
"""
import typing


def element_length(
        lst: typing.Iterable[typing.Sequence]
        ) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    Retourne une liste de tuples contenant chaque élément et sa longueur.
    """
    return [(i, len(i)) for i in lst]
