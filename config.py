

LOG_SETTINGS = {
    'version': 1,
    'root': {
        'level': 'INFO',
        'handlers': ['file'],
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'normal',
            'filename': 'sonos_sleep.log',
            'mode': 'a',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
    },
    'formatters': {
        'normal': {
            'format': '%(asctime)s %(levelname)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
}


SONOS_DEVICE_NAME = "Master Bedroom"
DEFAULT_VOLUME = 10
DEFAULT_SLEEP_TIME_MINUTES = 15
DEFAULT_WAIT_FOR_SLEEP_TIME_TO_BE_SET_IN_MINUTES = 0
