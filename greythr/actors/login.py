from core.actor import Actor
from core.helper import is_login_button
from core.details import Details
from selenium.webdriver.common.by import By
import logging
import time


class IsLoginPageLoaded(Actor):
    def act(self, driver):
        user_input = driver.find_element(By.ID, "username")
        return user_input is not None


class PerformLoginOperation(Actor):
    def __init__(self, details: Details):
        self.details = details

    def act(self, driver):
        user_in, pass_in, login_btn = self.find_elements(driver)
        if is_login_button(login_btn.text):
            user_in.send_keys(self.details.username)
            pass_in.send_keys(self.details.password)
            login_btn.click()
        time.sleep(5.0)

    @staticmethod
    def find_elements(driver):
        logging.info("fetcing username input box element ... ")
        user_input = driver.find_element(By.ID, "username")
        logging.info("fetching password input box element ... ")
        pass_input = driver.find_element(By.ID, "password")
        logging.info("fetching login button element ... ")
        login_btn = driver.find_element(By.TAG_NAME, "button")
        return user_input, pass_input, login_btn
