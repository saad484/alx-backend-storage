#!/usr/bin/env python3

"""
function to update school collection
"""


def update_topics(mongo_collection, name, topics):
    """
    func doc
    """
    return mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
            )
