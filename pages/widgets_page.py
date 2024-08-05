import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generate_color, generate_date
from locators.widgets_page_locators import AccordianPageLocators, AutocompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPagelocators, ToolTipsPageLocators, MenuPageLocators
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
        try:
            color_list = self.elements_are_present(self.locators.MULTI_COMPLETE_VALUES, timeout=2)
        except TimeoutException:
            color_list = []
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def clear_all_multi(self):
        """Clear all multiselect values."""
        self.element_is_visible(self.locators.MULTI_CLEAR_VALUES).click()

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


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def set_date(self):
        """Sets the date in the date input field.

        Returns:
            tuple: A tuple containing the date value before and after the update.
        """
        date = next(generate_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        date_before = input_date.get_attribute('value')
        input_date.click()

        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        time.sleep(2)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        time.sleep(2)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY, date.day)

        date_after = input_date.get_attribute('value')
        return date_before, date_after

    def set_datetime(self):
        """
        Sets the date and time in the datetime input field.

        Returns:
            tuple: A tuple containing the datetime value before and after the update.
        """
        date = next(generate_date())
        input_date = self.element_is_visible(self.locators.DATETIME_INPUT)
        date_before = input_date.get_attribute('value')
        input_date.click()

        # Month
        self.element_is_visible(self.locators.DATETIME_SELECT_MONTH).click()
        time.sleep(1)
        self.set_date_item_from_list(self.locators.DATETIME_SELECT_MONTH_LIST, date.month)
        time.sleep(1)
        # Year
        self.element_is_visible(self.locators.DATETIME_SELECT_YEAR).click()
        time.sleep(1)
        self.set_date_item_from_list(self.locators.DATETIME_SELECT_YEAR_LIST, date.year)
        time.sleep(1)
        # Day
        self.set_date_item_from_list(self.locators.DATETIME_SELECT_DAY, date.day)
        time.sleep(1)
        # Time
        self.set_date_item_from_list(self.locators.DATETIME_SELECT_TIME_LIST, date.time)

        date_after = input_date.get_attribute('value')
        return date_before, date_after


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):
        """Changes the value of a slider and retrieves its value before and after the change.

        Returns:
            tuple: A tuple containing the slider value before and after the change.

        """
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE_INPUT).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE_INPUT).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    def start_stop_progressbar(self):
        """Starts and stops the progress bar, then retrieves its value before and after.

        Returns:
            tuple: A tuple containing the progress bar value before and after the operation.
        """
        value_before = self.element_is_present(self.locators.PROGRESSBAR_VALUE_INPUT).text

        progressbar = self.element_is_clickable(self.locators.PROGRESSBAR_START_STOP_BUTTON)
        progressbar.click()
        time.sleep(random.randint(1, 5))
        progressbar.click()

        value_after = self.element_is_present(self.locators.PROGRESSBAR_VALUE_INPUT).text
        return value_before, value_after


class TabsPage(BasePage):
    """https://demoqa.com/tabs"""
    locators = TabsPagelocators()

    def get_tab_content(self, tab):
        """Clicks on a specified tab and retrieves the text content of that tab, along with the length of the content.

        Args:
            tab (str): The tab to retrieve content from. Options include 'What', 'Origin', 'Use', and 'More'.

        Returns:
            tuple: A tuple containing the text of the tab button and the length of the tab content.
        """
        tab_locators = {
            'What': (self.locators.TABS_WHAT, self.locators.TABS_WHAT_CONTENT),
            'Origin': (self.locators.TABS_ORIGIN, self.locators.TABS_ORIGIN_CONTENT),
            'Use': (self.locators.TABS_USE, self.locators.TABS_USE_CONTENT),
            'More': (self.locators.TABS_MORE, self.locators.TABS_MORE_CONTENT),
        }
        tab_button = self.element_is_visible(tab_locators[tab][0])
        tab_button.click()
        tab_content = self.element_is_visible(tab_locators[tab][1]).text
        return tab_button.text, len(tab_content)


class ToolTipsPage(BasePage):
    """https://demoqa.com/tool-tips"""
    locators = ToolTipsPageLocators()

    def get_tooltip_text(self, hover_to):
        """Hovers over a specified element to trigger its tooltip and then retrieves the tooltip text.

        Args:
            hover_to (str): The element to hover over. Options include 'Button', 'Field', 'Contrary', and 'Section'.

        Returns:
            str: The text of the tooltip.
        """
        hover_locators = {
            'Button': {
                'element': self.locators.HOVER_BUTTON,
                'tooltip': self.locators.HOVER_TOOLTIP_BUTTON
            },
            'Field': {
                'element': self.locators.HOVER_FIELD_INPUT,
                'tooltip': self.locators.HOVER_FIELD_TOOLTIP_INPUT
            },
            'Contrary': {
                'element': self.locators.HOVER_CONTRARY_LINK,
                'tooltip': self.locators.HOVER_CONTRARY_TOOLTIP_LINK
            },
            'Section': {
                'element': self.locators.HOVER_SECTION_LINK,
                'tooltip': self.locators.HOVER_SECTION_TOOLTIP_LINK
            },
        }
        element = self.element_is_present(hover_locators[hover_to]['element'])
        self.action_move_to_element(element)
        time.sleep(2)
        self.element_is_visible(hover_locators[hover_to]['tooltip'])
        tooltip_text = self.element_is_visible(self.locators.TOOLTIP_INNER_DIV).text
        return tooltip_text


class MenuPage(BasePage):
    """https://demoqa.com/menu"""
    locators = MenuPageLocators()

    def get_menu_items(self):
        """Return a list of text from all menu items on the page."""
        menu = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu:
            self.action_move_to_element(item)
            data.append(item.text)
        return data
