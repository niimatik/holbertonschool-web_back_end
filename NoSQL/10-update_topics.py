#!/usr/bin/env python3
"""
Module for updating the topics of a school document in MongoDB.
"""


def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a school document based on the school's name.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
