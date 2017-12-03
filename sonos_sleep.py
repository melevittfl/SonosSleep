import soco
from soco.discovery import by_name
from time import sleep
import datetime
import fcntl
import sys
import errno
import logging
import logging.config
from config import *


def seconds_to_minutes_and_seconds(seconds):
    return datetime.datetime.fromtimestamp(seconds).strftime('%M minutes %S seconds')


def main():
    device = by_name(SONOS_DEVICE_NAME)
    status = device.get_current_transport_info()['current_transport_state']
    logging.debug(f"Sonos {SONOS_DEVICE_NAME} device is {status}")
    if status == "PLAYING":
        logging.info(f"{SONOS_DEVICE_NAME} is Playing")
        if device.volume > DEFAULT_VOLUME:
            logging.info(f"Volume at {device.volume}. Setting volume to {DEFAULT_VOLUME}")
            device.ramp_to_volume(DEFAULT_VOLUME)
        if not device.get_sleep_timer():
            pause_time = DEFAULT_WAIT_FOR_SLEEP_TIME_TO_BE_SET_IN_MINUTES * 60
            sleep_time = DEFAULT_SLEEP_TIME_MINUTES * 60
            logging.info(f"Sleep timer not set. Pausing for {seconds_to_minutes_and_seconds(pause_time)}")
            sleep(pause_time)
            if not device.get_sleep_timer():
                logging.info(f"Sleep timer still not set after {seconds_to_minutes_and_seconds(pause_time)}. Setting sleep timer to {seconds_to_minutes_and_seconds(sleep_time)}")
                device.set_sleep_timer(sleep_time)
            else:

                logging.info(f"Sleep timer was set by a human")
        else:
            logging.info("Sleep timer already set")
        sleep_time = device.get_sleep_timer()
        logging.info(f"Sleep timer set to {seconds_to_minutes_and_seconds(sleep_time)}")


if __name__ == '__main__':
    logging.config.dictConfig(LOG_SETTINGS)
    logging.debug("Checking Sonos")

    f = open('.lock', 'w')
    try:
        fcntl.lockf(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError as e:
        if e.errno == errno.EAGAIN:
            logging.error("Another instance already running")
            sys.exit(-1)

    main()

