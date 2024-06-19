#!/usr/bin/env python3
'''
doc doc Module
'''

import redis
import uuid
from typing import Union

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

    def store(slef, data: Union[str, bytes, int, float]) -> str:
        '''
        doc doc method
        '''
        keyx = str(uuid.uuid4())
        slef._redis.set(keyx, data)
        return keyx
