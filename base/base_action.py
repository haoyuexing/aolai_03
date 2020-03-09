from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10.0, poll=1.0):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*feature))

    def click(self, feature, timeout=10.0, poll=1.0):
        self.find_element(feature, timeout, poll).click()

    def input(self, feature, text, timeout=10.0, poll=1.0):
        self.clear(feature, timeout, poll)
        self.find_element(feature, timeout, poll).send_keys(text)

    def clear(self, feature, timeout=10.0, poll=1.0):
        self.find_element(feature, timeout, poll).clear()

    def get_text(self, feature, timeout=10.0, poll=1.0):
        return self.find_element(feature, timeout, poll).text

    def is_toast_exist(self, text):
        try:
            self.find_element((By.XPATH, "//*[@contains," + text + "]"), 5, 0.1)
            return True
        except Exception as e:
            return False