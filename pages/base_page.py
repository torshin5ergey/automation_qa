from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    # Initialize the BasePage class with a WebDriver instance and a URL
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        # Open the URL in the WebDriver browser instance
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        """
        Wait until the element identified by the locator becomes visible on the webpage.

        :param locator: A tuple (By, value) identifying the element to wait for.
        :param timeout: Maximum time to wait for the element to become visible (default is 5 seconds).
        :return: The located WebElement once it is visible.
        """
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        """
        Wait until all elements identified by the locator become visible on the webpage.

        :param locator: A tuple (By, value) identifying the elements to wait for.
        :param timeout: Maximum time to wait for the elements to become visible (default is 5 seconds).
        :return: The list of located WebElements once all are visible.
        """
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        """
        Wait until the element identified by the locator becomes present in the DOM of the webpage.

        :param locator: A tuple (By, value) identifying the element to wait for.
        :param timeout: Maximum time to wait for the element to become present (default is 5 seconds).
        :return: The located WebElement once it is present.
        """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        """
        Wait until all elements identified by the locator become present in the DOM of the webpage.

        :param locator: A tuple (By, value) identifying the elements to wait for.
        :param timeout: Maximum time to wait for the elements to become present (default is 5 seconds).
        :return: The list of located WebElements once all are present.
        """
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        """
        Wait until the element identified by the locator becomes invisible on the webpage.

        :param locator: A tuple (By, value) identifying the element to wait for.
        :param timeout: Maximum time to wait for the element to become invisible (default is 5 seconds).
        :return: True once the element is invisible.
        """
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        """
        Wait until the element identified by the locator becomes clickable on the webpage.

        :param locator: A tuple (By, value) identifying the element to wait for.
        :param timeout: Maximum time to wait for the element to become clickable (default is 5 seconds).
        :return: The located WebElement once it is clickable.
        """
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        """
        Scroll the webpage to bring the specified element into view.

        :param element: The WebElement to scroll to.
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
