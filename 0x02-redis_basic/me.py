#!/usr/bin/env python3
from uuid import uuid4
from typing import Union
import redis
class Cache:
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        rdmkey = str(uuid4())
        self._redis.set(rdmkey, data)
        return rdmkey


cache = Cache()
data = b"hello"
key = cache.store(data)
print(key)

local = redis.Redis()
print(local.get(key))
