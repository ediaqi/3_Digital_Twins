import logging
import time
from datetime import datetime, timezone

import pytz

import settings


class CustomFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        current_time = datetime.fromtimestamp(record.created)
        if datefmt:
            ts = current_time.strftime(datefmt)
        else:
            t = current_time.astimezone()
            t = t.replace(microsecond=int(1000 * record.msecs))
            timestamp = t.strftime("%Y-%m-%d %H:%M:%S.%f%z")
            ts = "%s" % (timestamp)
        return ts


def format_logger(logger):
    ch = logging.StreamHandler()
    formatter = CustomFormatter(fmt='[%(asctime)s] %(levelname)8s: [%(name)s] - %(message)s')
    ch.setFormatter(formatter)

    # disable duplicate logging because of parent module loggers
    logger.propagate = False
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(ch)

    logger.setLevel(settings.LOG_LEVEL)


def get_current_iso_time(tz="UTC") -> str:
    dt = datetime.utcnow()
    dt = dt.replace(tzinfo=pytz.UTC)
    dt = dt.astimezone(pytz.timezone(tz)).isoformat()
    return dt


def uppercase_first(string):
    return string[0].upper() + string[1:]


def timeit(method):
    def timed(*args, **kwargs):
        ts = time.perf_counter()
        result = method(*args, **kwargs)
        logging.debug("%50s: %5.1f ms" % (str(method).split(' ')[1], (time.perf_counter() - ts) * 1000))
        return result
    return timed
