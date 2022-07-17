from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from core.actor import Actor


class ChromeDriver:

    def __init__(self, headless=False):
        self.options = self.generate_options(headless)
        self.driver = self.generate_driver(self.options)

    def do(self, actor):
        return actor(self.driver)

    def do(self, actor: Actor):
        return actor.act(self.driver)

    def close(self):
        self.driver.close()

    @staticmethod
    def generate_options(headless: bool):
        options = Options()
        options.add_argument("--incognito")
        if headless:
            options.add_argument("--headless")
        return options

    @staticmethod
    def generate_driver(options):
        return webdriver.Chrome(options=options)
