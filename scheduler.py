"""This module provides a Scheduler class for running functions periodically."""

import time
import schedule


class Scheduler:
    """This is Scheduler class and it will run the function in every seconds that you give."""

    def __init__(self, func):
        self.func = func

    def every(self, seconds: int) -> None:
        """This function schedules the function to run every given seconds."""
        schedule.every(seconds).seconds.do(self.func)

    def run(self) -> None:
        """This function starts scheduling loop and runs pending tasks."""
        while True:
            schedule.run_pending()
            time.sleep(1)
