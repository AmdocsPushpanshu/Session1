# noinspection SpellCheckingInspection
class HomePage():
    # Constructor with elements defination and pass the driver which we will
    # work with in test cases

    def __init__(self, driver):
        self.driver = driver

        # Create locators for elements on webpage to work with
        self.welcomelink_id = "welcome"
        self.logout_linktext = "Logout"

    # Functions for actions that will be done on the webpage
    def user_logout(self):
        self.driver.find_element_by_id(self.welcomelink_id).click()
        self.driver.find_element_by_link_text(self.logout_linktext).click()