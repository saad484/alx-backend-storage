#!/usr/bin/env python3

"""
function to update school collection
"""


def schools_by_topic(mongo_collection, topic):
    """
    func doc
    """
    return mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
            )
