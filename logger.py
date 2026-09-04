"""This module provides a Logger class for logging messages."""

import logging


class Logger:
    """This Logger class is used to log messages with different levels."""

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def info(self, msg: str) -> None:
        """This function shows a log message with info level"""
        self.logger.info(msg=msg)

    def warning(self, msg: str) -> None:
        """This function shows a log message with warning level"""
        self.logger.warning(msg=msg)

    def error(self, msg: str) -> None:
        """This function shows a log message with error level"""
        self.logger.error(msg=msg)

    def debug(self, msg: str) -> None:
        """This function shows a log message with debug level"""
        self.logger.debug(msg=msg)
