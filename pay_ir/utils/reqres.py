"""
    This module contains utility functions to
        deal with requests/response objects, etc.
"""

import json


def get_json(response):
    """
        Parses a returned response as json when sending a request
            using 'requests' module.
    """

    return json.loads(response.content.decode('utf-8'))
