import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store",default="chrome",help="Please pass the browser name like python -m pytest --browser chrome")

@pytest.fixture(scope="class")
def test_setup(request):

    # Get the browser from command line and do activity
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(
            executable_path="C:/01 - Self Learnings/Python And Selenium/PyCharm Selenium Projects/Selenium Projects/FrameWorks/Session1/drivers/chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(
            executable_path="C:/01 - Self Learnings/Python And Selenium/PyCharm Selenium Projects/Selenium Projects/FrameWorks/Session1/drivers/geckodriver.exe")
    else:
        print("Please enter an valid browser - either chrome or firefox")

    driver.implicitly_wait(20)
    driver.maximize_window()
    request.cls.driver = driver

    # Tear Down
    yield
    driver.close()
    driver.quit()
    print("Test Completed")