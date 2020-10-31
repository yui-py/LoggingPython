import logging
from logger import configure_logger
from bar import bar
from foo import foo

logger = logging.getLogger(__name__)
configure_logger(logging.DEBUG)
logger.info('Hello World!!')
bar.say_hi()
foo.say_hi()
