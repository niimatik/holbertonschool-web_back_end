#!/usr/bin/env python3
"""
Module that defines a function to list all documents in a MongoDB collection
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    """
    documents = list(mongo_collection.find())
    return documents
