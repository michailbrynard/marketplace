import os

CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = "UTC"

CELERY_CREATE_MISSING_QUEUES = True
CELERY_PREFETCH_MULTIPLIER = 1

HOST_NAME = os.environ.get('HOST_NAME', 'local')

default_queue = '-'.join(('general', HOST_NAME))
CELERY_DEFAULT_QUEUE = default_queue

BROKER_TRANSPORT = 'sqs'
BROKER_TRANSPORT_OPTIONS = {
    'region': 'eu-west-1',
    'visibility_timeout': 43200,
    'polling_interval': 1,
}
