#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.__dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """gets hyper_index returns a dict"""
        # if index is None, start from the beginning
        if index is None:
            index = 0
        assert 0 <= index < len(self.__dataset)  # verifies idx is valid range
        # find the en index for the page
        end_index = index
        page_data = []
        while len(page_data) < page_size and end_index < len(self.__dataset):
            if end_index in self.__dataset:
                page_data.append(self.__dataset[end_index])
            end_index += 1
        # find the next page
        next_index = end_index
        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": page_data
        }
