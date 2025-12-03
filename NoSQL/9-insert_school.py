#!/usr/bin/env python3
"""
Insert a new document into a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into the given MongoDB collection.

    """
    posts = mongo_collection.insert_one(kwargs)
    return posts.inserted_id
