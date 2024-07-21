from pages.base_page import BasePage
from locators.afw_page_locators import BrowserWindowsPageLocators


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def get_new_opened_tab_header(self, open_as='tab'):
        """Open a new tab or window and get the header of the new page.

        Args:
            open_as (str): Specify 'tab' to open in a new tab, or 'window' to open in a new window.

        Returns:
            str: The header of the new page.
        """
        if open_as == 'tab':
            self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        elif open_as == 'window':
            self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()

        self.driver.switch_to.window(self.driver.window_handles[-1])
        new_page_header = self.element_is_present(self.locators.NEW_PAGE_HEADER).text
        return new_page_header
