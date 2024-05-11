import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Fixture providing a WebDriver instance for each test
@pytest.fixture()
def driver():
    # Initializing the Edge driver using WebDriver Manager
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    # Maximizing the browser window size
    driver.maximize_window()
    # Returning the driver for use in tests
    yield driver
    # Quitting the browser session after the test execution
    driver.quit()
