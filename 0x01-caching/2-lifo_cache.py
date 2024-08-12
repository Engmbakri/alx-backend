#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching and is a caching system
        that uses the LIFO (Last-In, First-Out) algorithm.
    """

    def __init__(self):
        """ Initialize the class with the parent init method and a list to
            track the insertion order of keys.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache using LIFO strategy.
            If key or item is None, do nothing.
            If the number of items in cache_data exceeds MAX_ITEMS, discard
            the last added item (LIFO) and print the discarded key.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.order.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """ Get an item by key.
            If key is None or doesn't exist in cache_data, return None.
        """
        return self.cache_data.get(key, None)
