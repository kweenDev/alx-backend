#!/usr/bin/env python3
"""
BasicCache Module - No limit caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache implements a simple caching system without any limit on cache
    size.
    """

    def put(self, key, item):
        """
        Adds an item to the cache.
        Parameters:
            key (str): Key for the item.
            item (Any): The item to store.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache.
        Parameters:
            key (str): The key for the item to retrieve.
        Returns:
            The cached item or None if the key doesn't exist.
        """
        return self.cache_data.get(key, None)
