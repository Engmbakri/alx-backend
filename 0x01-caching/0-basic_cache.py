#!/usr/bin/env python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching and is a caching system
        that doesn't have any limit.
    """

    def put(self, key, item):
        """ Add an item in the cache
            If key or item is None, do nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
            If key is None or doesn't exist in cache, return None.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
