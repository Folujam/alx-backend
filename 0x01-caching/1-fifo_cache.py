#!/usr/bin/env python3
"""LIFO Caching Module"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """inherits from base caching lol duh!
    -its a caching system
    -it implements a put and get method"""
    def __init__(self):
        """initializes this cache and base cache
        -orders the dict(cache_data) so as to pop pricisely"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """if key is empty nothing is done
        -key in data assigns item
        -if memory filled old item is popped for new item"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # fist_key = list(self.cache_data.keys())[1] only returns value
            popped_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", popped_key)

    def get(self, key):
        """checks if key value exist
        - returns key value"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
