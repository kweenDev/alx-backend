#!/usr/bin/env python3
"""
FIFOCache Module - First In First Out caching system
"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    FIFOCache implements a caching system using First In First Out
    (FIFO) policy.
    """

    def __init__(self):
        """
        Initializes FIFOCache.
        """
        super().__init__()
        self.cache_data = OrderedDict()
