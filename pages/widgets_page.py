import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generate_color
from locators.widgets_page_locators import AccordianPageLocators, AutocompletePageLocators
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


class AutocompletePage(BasePage):
    """https://demoqa.com/auto-complete"""
    locators = AutocompletePageLocators()

    def add_value_multi(self, num=1):
        """Add multiple values to the multi-select input field.

        Args:
            num (int): The number of values to add (default is 1).

        Returns:
            list: A list of colors added to the multi-select input field.
        """
        colors = random.sample(next(generate_color()).color_name, k=num)
        for value in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_COMPLETE_INPUT)
            input_multi.send_keys(value)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_multi(self, num=1):
        """Remove a specified number of values from the multi-select input field.
        Note: The `num` should be less than the current number of selected elements by 1.

        Args:
            num (int): The number of values to remove (default is 1).

        Returns:
            tuple: A tuple containing the count of values before and after removal.
        """
        count_values_before = len(self.elements_are_present(self.locators.MULTI_COMPLETE_VALUES))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_COMPLETE_VALUE_REMOVE)
        for i in range(num):
            remove_button_list[i].click()
        count_values_after = len(self.elements_are_present(self.locators.MULTI_COMPLETE_VALUES))
        return count_values_before, count_values_after

    def get_current_multi_selection(self):
        """Get the current selection of colors from the multi-select input field.

        Returns:
            list: A list of colors currently selected in the multi-select input field.
        """
        color_list = self.elements_are_present(self.locators.MULTI_COMPLETE_VALUES)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    # TODO: delete all

    def add_value_single(self):
        """Add a value to the single-select input field.

        Returns:
            str: The color added to the single-select input field.
        """
        color = random.sample(next(generate_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_COMPLETE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def get_current_single_selection(self):
        """Get the current selection from the single-select input field.

        Returns:
            str: The color currently selected in the single-select input field.
        """
        color = self.element_is_visible(self.locators.SINGLE_COMPLETE_VALUE)
        return color.text
