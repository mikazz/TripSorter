# project/server/main/tasks.py

import time
import datetime

# Database Management
from project.server.models import Job
# Get rq context
from rq.job import get_current_job
# Graph handling
import networkx


def create_task(graph):
    """
    # Trip Madrid > New York JFK
    graph_before=[
        {"order" : ("Stockholm", "New York JFK")},
        {"order" : ("Barcelona", "Girona Airport")},
        {"order" : ("Madrid", "Barcelona")},
        {"order" : ("Girona Airport", "Stockholm")},
        ]

    graph_after=[
        {"order" : ("Madrid", "Barcelona")},
        {"order" : ("Barcelona", "Girona Airport")},
        {"order" : ("Girona Airport", "Stockholm")},
        {"order" : ("Stockholm", "New York JFK")},]
    """
    graph_before = graph
    edges = [tuple(*d.values()) for d in graph_before]
    # [('Stockholm', 'New York JFK'), ('Barcelona', 'Girona Airport')...
    G = networkx.DiGraph()
    G.add_edges_from(edges)

    longest_path = networkx.dag_longest_path(G)
    graph_after = list(zip(longest_path[:-1], longest_path[1:]))
    graph_after = [{'order': edge} for edge in graph_after]

    job_id = get_current_job().id
    # Get job
    job = Job.objects.get(job_id=job_id)

    # Edit
    job.job_is_finished = True
    job.job_ended_at = datetime.datetime.now()
    job.job_is_queued = False
    job.job_is_started = False
    job.job_status = "finished"
    job.graph = graph_after

    job.save()
    return True


# def create_task_2(task_type):
#     time.sleep(int(task_type) * 10)
#     job_id = get_current_job().id
#     # Get job
#     job = Job.objects.get(job_id=job_id)
#
#     # Edit
#     job.job_is_finished = True
#     job.job_ended_at = datetime.datetime.now()
#     job.job_is_queued = False
#     job.job_is_started = False
#     job.job_status = "finished"
#
#     job.save()
#     return True