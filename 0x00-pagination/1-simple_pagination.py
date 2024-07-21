#!/usr/bin/env python3
"""A helper Module"""
import csv
import math
from typing import List, Tuple 


def index_range(page: int, page_size: int) -> Tuple:
    """this function returns a tuple(start_index, end_index)"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

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
        """func gets 10 page data_set"""
        if page >= 1 or page_size <= 10:
            assert isinstance(page, int)
            assert page > 0
            assert isinstance(page_size, int)
            assert page_size > 0
            start_index, end_index = index_range(page, page_size)
            data_set = self.dataset()
            if start_index > len(data_set):
                return []
            return data_set[start_index:end_index]