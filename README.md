# SentryWithDjango

1. Install Sentry server on Docker
 * docker run -d --name sentry-redis redis
 * docker run -d --name sentry-postgres -e POSTGRES_PASSWORD=secret -e POSTGRES_USER=sentry postgres
 * docker run --rm sentry config generate-secret-key
 * docker run -it --rm -e SENTRY_SECRET_KEY='<secret-key>' --link sentry-postgres:postgres --link sentry-redis:redis sentry upgrade
 * docker run -d -p 8080:9000 --name my-sentry -e SENTRY_SECRET_KEY='<secret-key>' --link sentry-redis:redis --link sentry-postgres:postgres sentry
 * docker run -d --name sentry-cron -e SENTRY_SECRET_KEY='<secret-key>' --link sentry-postgres:postgres --link sentry-redis:redis sentry run cron
 * docker run -d --name sentry-worker-1 -e SENTRY_SECRET_KEY='<secret-key>' --link sentry-postgres:postgres --link sentry-redis:redis sentry run worker


2. Set raven on Django
 * pip install raven
 * Modify settings.py
```
INSTALLED_APPS = (
    'raven.contrib.django.raven_compat',
)

LOGGING = {
    ...
    'handlers': {
        'sentry': {
            'level': 'ERROR', # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    '''
```

 * Usage
```
logger.error('error test', exc_info=True, extra={
    'request': request,
})
```


