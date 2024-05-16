import random
import time

from selenium.webdriver.common.by import By

from generator.generator import generate_person
from locators.elements_page_locators import TextBoxLocators, CheckBoxLocators, RadioButtonLocators, WebTableLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):  # TextBoxPage, inheriting from BasePage
    locators = TextBoxLocators  # Setting locators attribute to TextBoxLocators class for element locators

    def fill_all_fields(self):
        """
        Fill all form fields with auto-generated data.

        :return: full name, email, current address, permanent address.
        :rtype: tuple
        """
        person_info = next(generate_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME, ).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        """
        Verify the filled form data by extracting text from displayed form fields.

        :return: full name, email, current address, permanent address extracted from the form.
        :rtype: tuple
        """
        full_name = self.element_is_present(self.locators.OUTPUT_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.OUTPUT_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.OUTPUT_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.OUTPUT_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):  # CheckBoxPage, inheriting from BasePage
    locators = CheckBoxLocators  # Setting locators attribute to CheckBoxLocators class for element locators

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

        :return: A formatted string with the text of checked checkboxes in lowercase, with spaces and ".doc" removed.
        :rtype: str
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

        :return: A formatted string with the text from the result field in lowercase, with spaces removed.
        :rtype: str
        """
        result_list = self.elements_are_visible(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).lower().replace(' ', '')


class RadioButtonPage(BasePage):  # RadioButtonPage, inheriting from BasePage
    locators = RadioButtonLocators()  # Setting locators attribute to RadioButtonLocators class for element locators

    def click_radio(self, choice):
        """
        Click random radio button.

        :param choice: The choice of radio button to click. It can be 'yes', 'impressive', or 'no'.
        :type choice: str
        """
        choices = {'yes': self.locators.RADIO_YES,
                   'impressive': self.locators.RADIO_IMPRESSIVE,
                   'no': self.locators.RADIO_NO}
        # Choice validation
        if choice not in choices:
            raise ValueError(f"Invalid choice: {choice}. Valid choices are: 'yes', 'impressive', 'no'.")
        # Click random radio
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        """
        Get the text from result field.

        :return: The text from presented output text field.
        :rtype: str
        """
        result_list = self.elements_are_visible(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return ''.join(data).lower().replace(' ', '')


class WebTablePage(BasePage):
    locators = WebTableLocators()  # Setting locators attribute to WebTableLocators class for element locators

    def add_new_person(self, count=1):
        """
        Add new count of persons to the web table

        :param count: The number of persons to add (default is 1).
        :type count: int
        :return: A list containing the details of the added persons.
        :rtype: list
        """
        while count != 0:
            person_info = next(generate_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    def check_added_person(self):
        """
        Retrieve the details of added persons from the web table.

        :return: A list containing the details of added persons.
        :rtype: list
        """
        person_list = self.elements_are_present(self.locators.FULL_PERSONS_LIST)
        data = []
        for item in person_list:
            data.append(item.text.splitlines())
        return data

    def search_person(self, keyword):
        """
        Search person with keyword.

        :param keyword:
        :return:
        """
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(keyword)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        parent_row = delete_button.find_element(*self.locators.PARENT_ROW)
        return parent_row.text.splitlines()
