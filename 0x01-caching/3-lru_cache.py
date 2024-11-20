#!/usr/bin/env python3
"""
LRUCache Module - Least Recently Used caching system
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRUCache implements a caching system using Least Recently Used
    (LRU) policy.
    """

    def __init__(self):
        """
        Initializes LRUCache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache, discarding the least recently used item if
        cache exceeds MAX_ITEMS.
        Parameters:
            key (str): Key for the item.
            item (Any): The item to store.
        """
        if key is not None and item is not None:
            if len(
                self.cache_data
            ) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                discarded_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {discarded_key}")
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item by key from the cache, marking it as recently used.
        Parameters:
            key (str): The key for the item to retrieve.
        Returns:
            The cached item or None if the key doesn't exist.
        """
        if key in self.cache_data:
            item = self.cache_data.pop(key)
            self.cache_data[key] = item
            return item
        return None
