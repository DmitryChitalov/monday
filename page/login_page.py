# https://the-internet.herokuapp.com/login
from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def auth_as(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
