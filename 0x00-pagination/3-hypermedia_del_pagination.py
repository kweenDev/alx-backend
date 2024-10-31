#!/usr/bin/env python3
"""
Deletion-resilient pagination with index tracking.
"""

import csv
from typing import List, Dict
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Load and cache dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Create an indexed version of the dataset for deletion resilience."""
        if self.__indexed_dataset is None:
            self.__indexed_dataset = {
                i: row for i, row in enumerate(self.dataset())
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve a page with deletion-resilient index tracking.

        Args:
            index (int): Starting index for the page.
            page_size (int): Number of items per page.

        Returns:
            Dict: Dictionary containing pagination data and metadata.
        """
        assert isinstance(index, int) and 0 <= index < len(self.dataset())
        data = []
        current_index = index
        next_index = index

        while len(
                data) < page_size and next_index < len(
                    self.indexed_dataset()):
            if next_index in self.indexed_dataset():
                data.append(self.indexed_dataset()[next_index])
            next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
