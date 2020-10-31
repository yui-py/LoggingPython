import logging

logger = logging.getLogger(__name__)


def say_hi():
    logger.info('Hi, foo')
    logger.debug('foo debug')
