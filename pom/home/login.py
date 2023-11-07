from selenium.webdriver.common.by import By
from base.browser_driver import BrowserDriver
from util.custom_logger import customLogger
import logging


class LoginPage(BrowserDriver):

    log = customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _emaid_field = 'username'
    _password_field = 'password'
    _login_button = 'submit'

    def getEmailField(self):
        return self.driver.find_element(By.ID, self._emaid_field)

    def getPasswordField(self):
        return self.driver.find_element(By.ID, self._password_field)

    def getLoginButton(self):
        return self.driver.find_element(By.ID, self._login_button)
    
    def enterEmail(self, username):
        # self.getEmailField().send_keys(username)
        self.senKeys(username, self._emaid_field)

    def enterPassword(self, password):
        # self.getPasswordField().send_keys(password)
        self.senKeys(password, self._password_field, locatorType='id')

    def clickLoginButton(self):
        # self.getLoginButton().click()
        self.elementClick(self._login_button, locatorType='id')

    def login(self, username, password):
        self.enterEmail(username)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSucessfull(self):
        return self.elementPresenceCheck('//*[@class="post-title"]', byType='xpath')