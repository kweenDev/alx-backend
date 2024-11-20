#!/usr/bin/env python3
"""
MRU Caching Module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache defines a caching system using the MRU algorithm."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.mru_key = None

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key.
        If the number of items exceeds MAX_ITEMS, discard the MRU item.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if key in self.cache_data:
            self.mru_key = key

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.mru_key:
                print(f"DISCARD: {self.mru_key}")
                del self.cache_data[self.mru_key]
                self.mru_key = None  # Reset MRU key

        def get(self, key):
            """
            Return the value linked to the key.
            If the key doesn't exist, return None.
            """
            if key is None or key not in self.cache_data:
                return None
        self.mru_key = key
        return self.cache_data[key]
