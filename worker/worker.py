#!/usr/bin/env python
"""
    Provides own worker script (instead of using rq worker)
    Worker will process to listen for queued jobs
"""

import sys

from sys import platform
from rq import Connection
from redis import Redis

if platform == "linux" or platform == "linux2":
    from rq import Worker  # best worker (has fork)
elif platform == "darwin":
    raise NotImplemented("Unknown rq job queue Worker for OS X")
elif platform == "win32":
    from rq_win import WindowsWorker as Worker  # Windows Worker (limited)


# Here you Can Preload libraries
# import library_that_you_want_preloaded
# from job import ...

# Provide queue names to listen to as arguments to this script, similar to rq worker
REDIS_URL = "redis://127.0.0.1:6379"
#REDIS_URL = "redis"

with Connection(connection=Redis()):
    qs = sys.argv[1:] or ['default']  # REDIS_QUEUES
    w = Worker(qs)
    w.work()
