from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    # Initialize the BasePage class with a WebDriver instance and a URL
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """Open the URL in the WebDriver browser instance."""
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        """Wait until the element identified by the locator becomes visible on the webpage.

        Args:
            locator (WebElement): The locator used to find the element.
            timeout (int): The maximum amount of time to wait for the element to be visible. Default is 5 seconds.

        Returns:
            WebElement: The WebElement once it is located and visible.
        """
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        """Wait until all elements identified by the locator become visible on the webpage.

        Args:
            locator (WebElement): The locator used to find the elements.
            timeout (int): The maximum amount of time to wait for the elements to be visible. Default is 5 seconds.

        Returns:
            list: A list of WebElements once they are located and visible.
        """
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        """Wait until the element identified by the locator becomes present in the DOM of the webpage.

        Args:
            locator (WebElement): The locator used to find the element.
            timeout (int): The maximum amount of time to wait for the element to be present. Default is 5 seconds.

        Returns:
            WebElement: The WebElement once it is located and present in the DOM.
        """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        """Wait until all elements identified by the locator become present in the DOM of the webpage.

        Args:
            locator (WebElement): The locator used to find the elements.
            timeout (int): The maximum amount of time to wait for the elements to be present. Default is 5 seconds.

        Returns:
            list: A list of WebElements once they are located and present in the DOM.
        """
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        """Wait until the element identified by the locator becomes invisible on the webpage.

        Args:
            locator (WebElement): The locator used to find the element.
            timeout (int): The maximum amount of time to wait for the element to be invisible. Default is 5 seconds.

        Returns:
            bool: True if the element becomes invisible within the timeout, otherwise False.
        """
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        """Wait until the element identified by the locator becomes clickable on the webpage.

        Args:
            locator (WebElement): The locator used to find the element.
            timeout (int): The maximum amount of time to wait for the element to be clickable. Default is 5 seconds.

        Returns:
            WebElement: The WebElement once it is located and clickable.
        """
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        """Scroll the webpage to bring the specified element into view.

        Args:
            element (WebElement): The WebElement to scroll into view.
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        """Double-click action on the specified element.

        Args:
            element (WebElement): The WebElement to double-click on.
        """
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        """Right-click action on the specified element.

        Args:
            element (WebElement): The WebElement to right-click on.
        """
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def switch_to_alert_window(self):
        """Switch the WebDriver's focus to the alert window.

        Returns:
            WebElement: The alert window.
        """
        return self.driver.switch_to.alert
