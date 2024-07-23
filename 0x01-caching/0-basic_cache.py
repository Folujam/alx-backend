#!/usr/bin/env python3
"""A simple CACHE Module"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """this class inherits from baseCaching"""
    def put(self, key, item):
        """assigns to dict value for key"""
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """returns value in key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
