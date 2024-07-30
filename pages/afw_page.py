import random
import time

from pages.base_page import BasePage
from locators.afw_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators


class BrowserWindowsPage(BasePage):
    """https://demoqa.com/browser-windows"""
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


class AlertsPage(BasePage):
    """https://demoqa.com/alerts"""
    locators = AlertsPageLocators()

    def get_alert_text(self, delay=0):
        if delay == 0:
            self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        elif delay > 0:
            self.element_is_visible(self.locators.APPEAR_IN_5SEC_ALERT_BUTTON).click()
            time.sleep(delay)
        alert_window = self.switch_to_alert_window()
        return alert_window.text

    def get_confirm_alert_text(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert_window()
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT_TEXT).text
        return text_result

    def get_prompt_alert_text(self):
        text = f"autotest{random.randint(0,999)}"
        self.element_is_visible(self.locators.PROMPT_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert_window()
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_RESULT_TEXT).text
        return text, text_result


class FramesPage(BasePage):
    """https://demoqa.com/frames"""
    locators = FramesPageLocators()

    def check_frame_num(self, frame_num):
        frame_locators = {
            'frame1': self.locators.FIRST_FRAME_IFRAME,
            'frame2': self.locators.SECOND_FRAME_IFRAME,
        }
        frame = self.element_is_present(frame_locators[frame_num])
        frame_width = frame.get_attribute('width')
        frame_height = frame.get_attribute('height')
        self.driver.switch_to.frame(frame)
        text = self.element_is_present(self.locators.FRAME_TITLE_HEADER).text
        self.driver.switch_to.default_content()
        return text, frame_width, frame_height
