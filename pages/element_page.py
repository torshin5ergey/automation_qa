import random
import time

from selenium.webdriver.common.by import By

from generator.generator import generate_person
from locators.elements_page_locators import TextBoxLocators, CheckBoxLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):  # TextBox page, inheriting from BasePage
    locators = TextBoxLocators  # Setting locators attribute to TextBoxLocators class for element locators

    def fill_all_fields(self):
        """
        Fill all form fields with auto-generated data.
        """
        person_info = next(generate_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME,).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        """
        Verify the filled form data by extracting text from displayed form fields.
        """
        full_name = self.element_is_present(self.locators.OUTPUT_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.OUTPUT_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.OUTPUT_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.OUTPUT_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):  # CheckBox page, inheriting from BasePage
    locators = CheckBoxLocators  # Setting locators attribute to CheckLocators class for element locators

    def open_full_list(self):
        """
        Toggle all checkbox list items.
        """
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        """
        Click random checkboxes.
        """
        # Getting the visible checkboxes list
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        repeats = 21  # Loop repeats
        # Random items selecting loop
        while repeats != 0:
            item = item_list[random.randint(1, item_list.len())]  # Select random item
            if repeats > 0:
                self.go_to_element(item)  # Scrolling to the selected checkbox
                item.click()
                repeats -= 1
            else:
                break

    def get_checked_checkboxes(self):
        """
        Get the text of checked checkboxes.
        """
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for checkbox in checked_list:
            item_title = checkbox.find_element(*self.locators.ITEM_TITLE)  # Finding elements with xpath
            data.append(item_title.text)
        return str(data).lower().replace(' ', '').replace('.doc', '')

    def get_output_result(self):
        """
        Gets the text from result field.
        """
        result_list = self.elements_are_visible(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).lower().replace(' ', '')
