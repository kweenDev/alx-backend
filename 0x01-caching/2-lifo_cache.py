#!/usr/bin/env python3
"""
LIFOCache Module - Last In First Out caching system
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache implements a caching system using Last In First Out
    (LIFO) policy.
    """

    def __init__(self):
        """
        Initializes LIFOCache.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache, discarding the most recent item if
        cache exceeds MAX_ITEMS.
        Parameters:
            key (str): Key for the item.
            item (Any): The item to store.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-1]
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item by key from the cache.
        Parameters:
            key (str): The key for the item to retrieve.
        Returns:
            The cached item or None if the key doesn't exist.
        """
        return self.cache_data.get(key, None)
