#!/usr/bin/env python3
"""
Module fournissant une fonction qui calcule un intervalle d’index
basé sur une page et une taille de page.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Retourne une structure contenant l’index de début et
    l’index de fin pour une page donnée.
    """
    index = []
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    index.append(start_index)
    index.append(end_index)
    return index
