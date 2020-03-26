import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils import utils
from selenium import webdriver

@pytest.mark.usefixtures("test_setup")
class TestOrangeHRMLogin():

    # Login Page Test
    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        # Create element of class LoginPage
        login = LoginPage(driver)
        login.user_login(utils.USERNAME, utils.PASSWORD)

    # Home Page Logout Test
    def test_logout(self):
        driver = self.driver
        logout = HomePage(driver)
        logout.user_logout()
