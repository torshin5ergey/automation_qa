import pytest
from selenium import webdriver

# MS Edge
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# Google Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# Fixture providing a WebDriver instance for each test
@pytest.fixture()
def driver():
    # Initializing the Edge driver using WebDriver Manager
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    # Initializing the Chrome driver using WebDriver Manager
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Maximizing the browser window size
    driver.maximize_window()
    # Returning the driver for use in tests
    yield driver
    # Quitting the browser session after the test execution
    driver.quit()
