import logging
from core.executor import WorkTimeLogExecutor
from core.details import Details
from scraper.chrome import ChromeDriver
from greythr.actors.loader import GreythrPageLoaderActor
from greythr.actors.login import IsLoginPageLoaded, PerformLoginOperation
from greythr.actors.timeaction import SignOutActor, SignInActor


class GreythrWorkTimeLogExecutor(WorkTimeLogExecutor):
    def __init__(self, details: Details, driver: ChromeDriver):
        super().__init__()
        self.details = details
        self.chrome = driver
        self.loader = GreythrPageLoaderActor()
        self.check_login_page_loaded = IsLoginPageLoaded()
        self.perform_login_op = PerformLoginOperation(details)
        self.sign_out_operation = SignOutActor()
        self.sign_in_operation = SignInActor()

    def workday_log_message(self):
        self.separator()
        logging.info("WORK DAY ... ")

    def holiday_log_message(self):
        self.separator()
        logging.info("HOLIDAY ... ")

    def load_login_page(self):
        self.chrome.do(self.loader)
        logging.info("LOADED LOGIN PAGE")

    def login(self):
        is_page_loaded: bool = self.chrome.do(self.check_login_page_loaded)
        if is_page_loaded:
            logging.info("login form detected")
            self.chrome.do(self.perform_login_op)
            logging.info("user login with username " + self.details.username)
        logging.info("USER LOGGED IN")

    def logout(self):
        logging.info("USER LOGGED OUT")
        self.chrome.close()

    def start_day(self):
        logging.info("STARTING THE DAY")
        self.chrome.do(self.sign_in_operation)

    def end_day(self):
        logging.info("ENDING THE DAY")
        self.chrome.do(self.sign_out_operation)

    @staticmethod
    def separator():
        logging.info("########################################################################")
