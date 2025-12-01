#!/usr/bin/env python3
"""
Module fournissant une fonction qui calcule un intervalle d’index basé
sur une page et une taille de page, et une classe serveur permettant
d’accéder à un jeu de données paginé.
"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Retourne une structure contenant l’index de début et
    l’index de fin pour une page donnée.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    index = (start_index, end_index)
    return index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retourne une portion du dataset correspondant
        à une page et une taille de page données.
        """
        assert isinstance(page) == int and page < 1
        assert isinstance(page_size) == int and page_size < 1
        start, end = index_range(page, page_size)
        data = self.dataset()
        return data[start:end]
