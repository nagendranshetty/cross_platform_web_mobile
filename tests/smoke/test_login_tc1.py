from selenium import webdriver
from selenium.webdriver.common.by import By
from pom.home.login import LoginPage
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestLoginTest():

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    def test_valid_login(self):
        self.lp.login('student', 'Password123')
        assert self.lp.verifyLoginSucessfull() == True
        print('Login sucessfull')

