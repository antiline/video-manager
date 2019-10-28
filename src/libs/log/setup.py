import logging.config
import sys

from libs.log.constants import LogLevel


def setup_logging(debug: bool = False) -> None:
    log_level = LogLevel.DEBUG if debug else LogLevel.INFO
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'json': {
                'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
                'datefmt': '%d/%b/%Y %H:%M:%S',
                'class': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            },
        },
        'handlers': {
            'stream': {
                'level': log_level,
                'class': 'logging.StreamHandler',
                'stream': sys.stderr,
                'formatter': 'json'
            },
        },
        'loggers': {
            '': {
                'handlers': ['stream', ],
                'level': log_level,
                'propagate': False,
            },
            'common': {
                'handlers': ['stream', ],
                'level': log_level,
                'propagate': False,
            },
            'request': {
                'handlers': ['stream'],
                'level': log_level,
            },
            'django': {
                'handlers': ['stream', ],
                'level': log_level,
                'propagate': False,
            },
            'django.request': {
                'handlers': ['stream'],
                'level': LogLevel.DEBUG if debug else LogLevel.ERROR,
                'propagate': False,
            },
            'django.template': {
                'handlers': ['stream'],
                'level': log_level,
                'propagate': False,
            },
        },
    })
