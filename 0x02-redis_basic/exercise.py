#!/usr/bin/env python3
'''
doc doc module
'''


import redis
import uuid
from typing import Union, Callable, Optional


class Cache():
    """
    doc doc class
    """

    def __init__(self):
        """
        doc doc method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        doc doc method
        '''
        keyx = str(uuid.uuid4())
        self._redis.set(keyx, data)
        return keyx

    def get(
            self, key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float]:
        '''
        doc doc method
        '''
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        '''
        doc doc method
        '''
        return self.get(key, fn=str)

    def get_int(self, key: int) -> int:
        '''
        doc doc method
        '''
        return self.get(key, fn=int)
