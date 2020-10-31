import logging

logger = logging.getLogger(__name__)


def say_hi():
    logger.info('Hi, bar')
    logger.warning('bar warning')
