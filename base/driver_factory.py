"""
@package base

DriverFactory class implementation
It creates a driver instance based on browser configurations

Example:
    wdf = DriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver

class DriverFactory():

    def __init__(self, browser):
        """
        Inits DriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseUrl = "https://practicetestautomation.com/practice-test-login/"

        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path="F:/Python Selenium Projects/Pytest_Projet_ex/Drivers/geckodriver.exe")

        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome(executable_path="D:/2023/cross_platform_web_mobile/tests/chromedriver.exe")
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseUrl)
        return driver