from selenium.common import TimeoutException

from locators.widgets_page_locators import AccordianPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    """https://demoqa.com/accordian"""
    locators = AccordianPageLocators()

    def get_section_data(self, section_name):
        section_locators = {
            1: (self.locators.FIRST_SECTION_HEADER, self.locators.FIRST_SECTION_TEXT),
            2: (self.locators.SECOND_SECTION_HEADER, self.locators.SECOND_SECTION_TEXT),
            3: (self.locators.THIRD_SECTION_HEADER, self.locators.THIRD_SECTION_TEXT),
        }
        section_title = self.element_is_visible(section_locators[section_name][0])
        try:
            section_text = self.element_is_visible(section_locators[section_name][1]).text
        except TimeoutException:
            section_title.click()
            section_text = self.element_is_visible(section_locators[section_name][1]).text

        return section_title.text, section_text
