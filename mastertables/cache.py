"""
Caching decorator
"""

import os
import sys
import json

from datetime import datetime as dt, timedelta as tdelta


def vocabulary_cache(func):
    CACHE_DIR = "/tmp/mastertables/"
    if sys.platform == "win32" or sys.platform == "cygwin":
        CACHE_DIR = "%(appdata)s\\mastertables\\" % {"appdata": os.getenv("APPDATA")}
    CACHE_NAME = "vocabulary_cache.json"
    CACHE_PATH = CACHE_DIR + CACHE_NAME

    CACHE_RESK = "response"  # cache response key
    CACHE_EXPK = "expires"  # cache expiration key
    CACHE_TIMEF = "%Y/%m/%d %H:%M:%S"  # time format
    CACHE_H = 0  # hours
    CACHE_M = 10  # minutes
    CACHE_S = 0  # seconds

    if not os.path.isdir(CACHE_DIR):
        os.makedirs(CACHE_DIR)
    if not os.path.isfile(CACHE_PATH):
        cache_file = open(CACHE_PATH, "w")
        cache_file.write("{}")
        cache_file.close()

    with open(CACHE_PATH, "r") as cache_file:
        cache = json.loads(cache_file.read())


    def call_api(*args, **kwargs):
        vocabulary = list(args)[1]  # fix: use keyword arguments !!!
        response = func(*args, **kwargs)
        expires = dt.now() + tdelta(hours=CACHE_H, minutes=CACHE_M, seconds=CACHE_S)
        cache[vocabulary] = {
            CACHE_RESK: response,
            CACHE_EXPK: dt.strftime(expires, CACHE_TIMEF)
        }

        with open(CACHE_PATH, "w") as cache_file:
            cache_file.write(json.dumps(cache, indent=2, sort_keys=True))


    def cached_func(*args, **kwargs):
        vocabulary = list(args)[1]  # fix: use keyword arguments !!!

        if vocabulary not in cache or dt.strptime(cache[vocabulary][CACHE_EXPK], CACHE_TIMEF) < dt.now():
            call_api(*args, **kwargs)

        return cache[vocabulary][CACHE_RESK]


    return cached_func
