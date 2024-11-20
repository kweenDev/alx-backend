#!/usr/bin/env python3
"""
LFU Caching Module
"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """LFUCache defines a caching system using the LFU algorithm."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.freq = defaultdict(int)
        self.usage_order = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key.
        If the number of items exceeds MAX_ITEMS, discard the LFU item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.freq[key] += 1
            self.usage_order.remove(key)
        else:
            self.cache_data[key] = item
            self.freq[key] = 1

        self.usage_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Find the LFU item(s)
            min_freq = min(self.freq.values())
            lfu_keys = [k for k, f in self.freq.items() if f == min_freq]

            # If there's a tie, use LRU logic
            for lfu_key in self.usage_order:
                if lfu_key in lfu_keys:
                    print(f"DISCARD: {lfu_key}")
                    del self.cache_data[lfu_key]
                    del self.freq[lfu_key]
                    self.usage_order.remove(lfu_key)
                    break

    def get(self, key):
        """
        Return the value linked to the key.
        If the key doesn't exist, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
