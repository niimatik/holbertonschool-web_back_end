#!/usr/bin/env python3
"""
Module that provides a function to retrieve schools by a specific topic
from a MongoDB collection.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieves a list of schools that have a specific topic.
    """
    result = list(mongo_collection.find({"topics": topic}))

    return result
