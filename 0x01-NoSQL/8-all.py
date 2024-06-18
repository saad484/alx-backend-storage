#!/usr/bin/python3
"""
list collection
"""


def list_all(mongo_collection):
    """
    func doc
    """
    return list(mongo_collection.find())
