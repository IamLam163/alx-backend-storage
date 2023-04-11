#!/usr/bin/env python
"""
function changes all topic of a school document based on name
"""


def update_topics(mongo_collection, name, topics):
    """function changes all topic of a school document based on name
    """
    mongo_collection.update_many({'name': name},
            {'$set': {'topics': topics}})
