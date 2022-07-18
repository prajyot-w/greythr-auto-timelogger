import logging
import multiprocessing
import time

from greythr.executor import GreythrWorkTimeLogExecutor
from core.details import Details
from scraper.chrome import ChromeDriver
from environment import LOG_FILE, LOG_FORMAT


def config():
    logging.basicConfig(filename=LOG_FILE,
                        level=logging.INFO,
                        format=LOG_FORMAT)


class Runner:
    def __init__(self, headless: bool = True):
        self.details = []
        self.headless = headless

    def addDetail(self, details: Details):
        self.details.append(details)

    def run(self):
        for detail in self.details:
            executor = GreythrWorkTimeLogExecutor(detail, ChromeDriver(headless=self.headless))
            executor.start()
            time.sleep(5.0)


if __name__ == '__main__':
    config()
    logging.info("**************** MAIN START ****************")
    runner = Runner(headless=True)
    runner.addDetail(Details("tb0097", "Techbulls@291295"))
    t = multiprocessing.Process(target=runner.run)
    t.start()
    logging.info("**************** MAIN END ****************")
