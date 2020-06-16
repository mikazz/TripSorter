# project/server/models.py

import datetime
from project.server import db


class Job(db.Document):
    """
    'job_id': job.get_id(),
    'job_status': job.get_status(),
    'job_result': job.result,
    'job_is_started': job.is_started,
    'job_started_at': job.started_at,
    'job_is_queued': job.is_queued,
    'job_timeout': job.timeout,
    'job_enqueued_at': job.enqueued_at,
    'job_ended_at': job.ended_at,
    'job_exc_info': job.exc_info,
    'job_dependent_ids': job.dependent_ids,
    'job_meta': job.meta,
    'job_func_name': job.func_name,
    'job_args': job.args,
    'job_kwargs': job.kwargs,
    """
    job_id = db.StringField(required=True, unique=True)
    job_status = db.StringField(required=True)
    job_result = db.StringField(required=False)
    job_is_started = db.BooleanField(required=False)
    job_is_finished = db.BooleanField(required=False)

    job_started_at = db.ComplexDateTimeField(required=False, default=datetime.datetime.now)
    job_is_queued = db.BooleanField(required=False)
    job_enqueued_at = db.ComplexDateTimeField(required=True)
    job_ended_at = db.ComplexDateTimeField(required=False)
    job_func_name = db.StringField(required=False)

    in_db_since = db.ComplexDateTimeField(default=datetime.datetime.now)
    job_timeout = db.IntField(required=False)

    graph = db.ListField(db.DictField(), required=False)

