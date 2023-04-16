#!/usr/bin/env python3
"""
Create a Cache class. In the __init__ method, store an instance of the Redis client as a private 
variable named _redis (using redis.Redis()) and flush the instance using flushdb.
Create a store method that takes a data argument and returns a string. The method should generate a random key 
(e.g. using uuid), store the input data in Redis using 
the random key and return the key.
"""

import redis
from typing import Callable, Optional, Union
from uuid import uuid4

class Cache:
    """class cache"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store method that takes an arg and returns a str"""
        rdmkey = str(uuid4())
        self._redis.set(rdmkey, data)
        return rdmkey


    def get(self, key: str, fn: Optional[Callable[[bytes], Union[str, bytes, int, float]]] = None) -> Union[str, bytes, int, float, None]:
            """get key and return data is fn is None"""
            data = self._redis.get(key)
            if data is None:
                    return None
            if fn is not None:
                    return fn(data)
            else:
                    return data

    def get_str(self, key: str) -> Union[str, bytes, int, float, None]:
             """automatically parametrize Cache.get with the correct conversion function"""
             data = self.get(key, lambda d: d.decode('utf-8'))
             return data


    def get_int(self, key: str) -> Union[str, bytes, int, float, None]:
             """automatically parametrize Cache.get with the correct conversion function"""
             # data = self.get(key, int)
             data = self.get(key, lambda d: int(d))
             return data


cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
