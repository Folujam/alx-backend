#!/usr/bin/env python3
"""LIFO Caching Module"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
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
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                # fist_key = list(self.cache_data.keys())[1] only returns value
                popped_key, _ = self.cache_data.popitem(last=True)
                print("DISCARD: {}".format(popped_key))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """checks if key value exist
        - returns key value"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
