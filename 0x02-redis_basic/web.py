#!/usr/bin/env python3
"""
doc doc module
"""

import requests as rq
from functools import wraps
from typing import Callable
import redis


redis_ = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """
        Decorator to Count
    """
    @wraps(method)
    def wrapper(url):
        """
        wrap for decoratot
        """
        redis_.incr(f"count:{url}")
        cached_html = redis_.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        redis_.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


def get_page(url: str) -> str:
    """
    doc doc method
    """
    req = rq.get(url)
    return req.text
