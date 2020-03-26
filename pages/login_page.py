# noinspection SpellCheckingInspection
from utils import utils
import moment

class LoginPage():

    # Constructor with elements defination and pass the driver which we will
    # work with in test cases
    def __init__(self, driver):
        # Pass the driver as argument
        self.driver = driver

        # Create locators for elements which test cases will work with
        self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"

    # Functions for actions that will happen on the this webpage
    def user_login(self, username,password):
        # Enter username
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

        # Enter password
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

        # Take a screenshot
        test_name = utils.whoami()
        timestamp = moment.now().strftime("%d%m%y_%H%M%S")
        screenshot_name = test_name + "_" + timestamp + ".png"
        self.driver.get_screenshot_as_file(
            "C:/01 - Self Learnings/Python And Selenium/PyCharm Selenium Projects/Selenium Projects/FrameWorks/Session1/screenshots/" + screenshot_name)

        # Click Login Button
        self.driver.find_element_by_id(self.login_button_id).click()