import random
import time

from selenium.webdriver.common.by import By

from generator.generator import generate_person
from locators.elements_page_locators import TextBoxLocators, CheckBoxLocators, RadioButtonLocators, WebTableLocators, \
    ButtonsLocators
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
            # Generating new person data
            person_info = next(generate_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            # Filling fields
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
        Return the details of added persons from the web table.

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
        :type keyword: str
        """
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(keyword)

    def check_search_person(self):
        """
        Check and return data about a person in a table row.

        :return: A list with person's data from the table row
        :rtype: list
        """
        # Finding person data with DELETE_BUTTON parent element by XPATH
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        parent_row = delete_button.find_element(*self.locators.PARENT_ROW)
        return parent_row.text.splitlines()

    def edit_person_info(self):
        """
        Edit person random data field and return edited data

        :return: Edited data
        :rtype: str
        """
        # Generating new person age data
        person_info = next(generate_person())
        # Selecting random person data field and getting its value
        random_field = random.choice(list(vars(person_info).keys()))
        data_to_edit = getattr(person_info, random_field)
        # Defining needed field locator
        fields_locators = {
            'firstname': self.locators.FIRST_NAME_INPUT,
            'lastname': self.locators.LAST_NAME_INPUT,
            'email': self.locators.EMAIL_INPUT,
            'age': self.locators.AGE_INPUT,
            'salary': self.locators.SALARY_INPUT,
            'department': self.locators.DEPARTMENT_INPUT
        }
        field_to_edit_locator = fields_locators[random_field]
        # Editing data
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(field_to_edit_locator).clear()
        self.element_is_visible(field_to_edit_locator).send_keys(data_to_edit)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return str(data_to_edit)

    def delete_person(self):
        """
        Delete a person's entry from the table.
        """
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted_person(self):
        """
        Check and return the deletion of a person's entry from the table.

        :return: Text of the label indicating no rows are found.
        :rtype str
        """
        return self.element_is_present(self.locators.NO_ROWS_FOUND_LABEL).text

    def change_displayed_rows_count(self):
        """
        Change the number of rows displayed per page and return the row count for each setting.

        :return: A list of actual row counts displayed for each setting.
        :rtype: list
        """
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for i in count:
            # Locate and scroll to the rows per page dropdown button
            rows_per_page_button = self.element_is_visible(self.locators.ROWS_PER_PAGE_SELECT)
            self.go_to_element(rows_per_page_button)
            # Click the dropdown button to open the options
            rows_per_page_button.click()
            # Select the option for the current count
            self.element_is_visible((By.CSS_SELECTOR, f"option[value='{i}']")).click()
            data.append(self.check_rows_per_page_count())
        return data

    def check_rows_per_page_count(self):
        """
        Check the number of rows currently displayed on the page.

        :return: The number of rows currently displayed on the page.
        :rtype: int
        """
        list_rows = self.elements_are_present(self.locators.FULL_PERSONS_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):
    locators = ButtonsLocators()

    def click_double_button(self):
        """
        Perform double-click action on the button and return output text.

        :return: The output text after the double-click action.
        :rtype: str
        """
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
        return self.check_clicked_buttons(self.locators.DOUBLE_CLICK_OUTPUT_RESULT)

    def click_right_button(self):
        """
        Perform a right-click action on the right-click button and return the result.

        :return: The output text after the right-click action.
        :rtype: str
        """
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
        return self.check_clicked_buttons(self.locators.RIGHT_CLICK_OUTPUT_RESULT)

    def click_dynamic_button(self):
        """
        Perform a click action on the dynamically loaded button and return the result.

        :return: The result text after the click action.
        :rtype: str
        """
        self.element_is_visible(self.locators.LEFT_CLICK_BUTTON).click()
        return self.check_clicked_buttons(self.locators.LEFT_CLICK_OUTPUT_RESULT)

    def check_clicked_buttons(self, element):
        """
        Check the result of the click actions by getting the text of the specified element.
        :param element: The locator of the element to check output result.
        :type element: WebElement
        :return: The text of the output for element.
        :rtype: str
        """
        return self.element_is_present(element).text
