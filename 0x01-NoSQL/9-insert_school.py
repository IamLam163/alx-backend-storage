#!/usr/bin/env python3
"""
python function that inserts a new document
"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new documentation"""
    new_doc = dict(kwargs)
    obj = mongo_collection.insert_one(new_doc)
    return obj.inserted_id
