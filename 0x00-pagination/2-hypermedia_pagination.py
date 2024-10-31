#!/usr/bin/env python3
"""
Server class with hypermedia pagination support.
"""

import math
import csv
from typing import List, Dict
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader][1:]
        return self.__dataset


def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
    """Retrieve a specific page of the dataset."""
    assert isinstance(page, int) and page > 0
    assert isinstance(page_size, int) and page_size > 0
    start, end = index_range(page, page_size)
    return self.dataset()[start:end]


def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
    """
    Retrieve a page and include pagination metadata.

    Args:
        page (int): Page number (1-indexed)
        page_size (int): Number of items per page.

    Returns:
        Dict: Dictionary containing page data and metadata.
    """
    data = self.get_page(page, page_size)
    total_pages = math.ceil(len(self.dataset()) / page_size)

    return {
        "page_size": len(data),
        "page": page,
        "data": data,
        "next_page": page + 1 if page < total_pages else None,
        "prev_page": page - 1 if page > 1 else None,
        "total_pages": total_pages
    }
