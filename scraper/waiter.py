from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitForElementByIdToLoad:
    def __init__(self, delay: int, html_id: str):
        self.delay = delay
        self.id = html_id

    def wait(self, driver):
        element = WebDriverWait(driver, self.delay)
        element.until(EC.presence_of_element_located((By.ID, self.id)))
