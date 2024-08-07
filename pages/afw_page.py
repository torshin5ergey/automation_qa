import random
import time

from pages.base_page import BasePage
from locators.afw_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogsPageLocators


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
        """Get the text of an alert.

        Args:
            delay (int): The delay in seconds before the alert appears.

        Returns:
            str: The text of the alert.
        """
        if delay == 0:
            self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        elif delay > 0:
            self.element_is_visible(self.locators.APPEAR_IN_5SEC_ALERT_BUTTON).click()
            time.sleep(delay)
        alert_window = self.switch_to_alert_window()
        return alert_window.text

    def get_confirm_alert_text(self):
        """Get the text result of a confirmation alert after accepting it.

        Returns:
            str: The result text after accepting the confirmation alert.
        """
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert_window()
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT_TEXT).text
        return text_result

    def get_prompt_alert_text(self):
        """Get the text entered into a prompt alert and the result text after accepting it.

        Returns:
            tuple: The entered text and the result text.
        """
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

    def get_frame_data(self, frame_name):
        """Get the text and dimensions of a specified frame.

        Args:
            frame_name (str): The name of the frame ('frame1' or 'frame2').

        Returns:
            tuple: The text within the frame and its width and height.
        """
        frame_locators = {
            'frame1': self.locators.FIRST_FRAME_IFRAME,
            'frame2': self.locators.SECOND_FRAME_IFRAME,
        }
        frame = self.element_is_present(frame_locators[frame_name])
        frame_width = frame.get_attribute('width')
        frame_height = frame.get_attribute('height')
        self.driver.switch_to.frame(frame)
        text = self.element_is_present(self.locators.FRAME_TITLE_HEADER).text
        self.driver.switch_to.default_content()
        return text, frame_width, frame_height


class NestedFramesPage(BasePage):
    """https://demoqa.com/nestedframes"""
    locators = NestedFramesPageLocators()

    def get_frames_text(self):
        """Get the text from both the parent and child frames.

        Returns:
            tuple: The text from the parent frame and the text from the child frame.
        """
        # Parent Frame
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME_IFRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_frame_text = self.element_is_present(self.locators.PARENT_FRAME_TEXT).text

        # Child Frame
        child_frame = self.element_is_present(self.locators.CHILD_FRAME_IFRAME)
        self.driver.switch_to.frame(child_frame)
        child_frame_text = self.element_is_present(self.locators.CHILD_FRAME_TEXT).text

        return parent_frame_text, child_frame_text


class ModalDialogsPage(BasePage):
    """https://demoqa.com/modal-dialogs"""
    locators = ModalDialogsPageLocators()

    def get_modal_data(self, modal_name):
        """Get the title and text of a specified modal.

        Args:
            modal_name (str): The name of the modal ('small' or 'large').

        Returns:
            tuple: The title and text of the specified modal.
        """
        modal_locators = {
            'small': (self.locators.SMALL_MODAL_BUTTON,
                      self.locators.SMALL_MODAL_TITLE,
                      self.locators.SMALL_MODAL_TEXT,
                      self.locators.SMALL_MODAL_CLOSE_BUTTON),
            'large': (self.locators.LARGE_MODAL_BUTTON,
                      self.locators.LARGE_MODAL_TITLE,
                      self.locators.LARGE_MODAL_TEXT,
                      self.locators.LARGE_MODAL_CLOSE_BUTTON),
        }
        self.element_is_visible(modal_locators[modal_name][0]).click()
        modal_title = self.element_is_visible(modal_locators[modal_name][1]).text
        modal_text = self.element_is_visible(modal_locators[modal_name][2]).text
        self.element_is_visible(modal_locators[modal_name][3]).click()
        return modal_title, modal_text
