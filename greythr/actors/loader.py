from core.actor import Actor
from greythr.constants import LOGIN_URL
from scraper.waiter import WaitForElementByIdToLoad
from selenium.common.exceptions import TimeoutException
import logging


class GreythrPageLoaderActor(Actor):
    def act(self, driver):
        self.load_page(driver)

    @staticmethod
    def load_page(driver):
        try:
            logging.info("attempting to load login page")
            driver.get(LOGIN_URL)
            waiter = WaitForElementByIdToLoad(65, "username")
            waiter.wait(driver)
        except TimeoutException as exp:
            logging.error("web page is taking too long to load.")
            logging.error(type(exp))
            logging.error(exp)

