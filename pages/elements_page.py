import os
import random
import time
from pathlib import Path

import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from generator.generator import generate_person, generate_file
from locators.elements_page_locators import TextBoxLocators, CheckBoxLocators, RadioButtonLocators, WebTableLocators, \
    ButtonsLocators, LinksPageLocators, UploadDownloadPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):  # https://demoqa.com/text-box
    locators = TextBoxLocators  # Setting locators attribute to TextBoxLocators class for element locators

    def fill_all_fields(self):
        """Fill all form fields with auto-generated data.

        Returns:
            tuple: Person data that auto-generated and filled the inputs.
            Each element is represented as a string. For example:

            ('Григорий Лаврентьев Денисович',
            'kovalevdemid@example.com',
            'п. Энгельс, наб. Ильича, д. 7/7 стр. 2/9, 164499',
            'д. Бирск, наб. Алтайская, д. 6 стр. 1, 176014'
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
        """Verify the filled form data by extracting text from form fields.

        Returns:
            tuple: Person data that extracted from form fields.
            Each element is represented as a string. For example:

            ('Григорий Лаврентьев Денисович',
            'kovalevdemid@example.com',
            'п. Энгельс, наб. Ильича, д. 7/7 стр. 2/9, 164499',
            'д. Бирск, наб. Алтайская, д. 6 стр. 1, 176014'
        """
        full_name = self.element_is_present(self.locators.OUTPUT_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.OUTPUT_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.OUTPUT_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.OUTPUT_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):  # https://demoqa.com/checkbox
    locators = CheckBoxLocators  # Setting locators attribute to CheckBoxLocators class for element locators

    def open_full_list(self):
        """Toggle all checkbox list items."""
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        """Click random checkboxes."""
        # Getting the visible checkboxes list
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        repeats = 21  # Loop repeats
        # Random items selecting loop
        while repeats != 0:
            item = item_list[random.randint(1, len(item_list))]  # Select random item
            if repeats > 0:
                self.go_to_element(item)  # Scrolling to the selected checkbox
                item.click()
                repeats -= 1
            else:
                break

    def get_checked_checkboxes(self):
        """Get the text of checked checkboxes.

        Returns:
            str: Formatted string with the text of checked checkboxes in lowercase, with spaces and ".doc" removed.
        """
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for checkbox in checked_list:
            item_title = checkbox.find_element(*self.locators.ITEM_TITLE)  # Finding elements with xpath
            data.append(item_title.text)
        return str(data).lower().replace(' ', '').replace('.doc', '')

    def get_output_result(self):
        """Gets the text from result field.

        Returns:
            str: Formatted string with the text from the result field in lowercase, with spaces removed.
        """
        result_list = self.elements_are_visible(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).lower().replace(' ', '')


class RadioButtonPage(BasePage):  # https://demoqa.com/radio-button
    locators = RadioButtonLocators()  # Setting locators attribute to RadioButtonLocators class for element locators

    def click_radio(self, choice):
        """Click a radio button based on the provided choice.

        Args:
            choice (str): The choice of radio button to click ('yes', 'impressive', or 'no').

        Raises:
            ValueError: If the provided choice is not 'yes', 'impressive', or 'no'.
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
        """Get the text from result field.

        Returns:
            str: The text from the presented output text field, formatted to be lowercase with spaces removed.
        """
        result_list = self.elements_are_visible(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return ''.join(data).lower().replace(' ', '')


class WebTablePage(BasePage):  # https://demoqa.com/webtables
    locators = WebTableLocators()  # Setting locators attribute to WebTableLocators class for element locators

    def add_new_person(self, count=1):
        """Add new count of persons to the web table.

        Args:
            count (int): The number of persons to add. The default is 1.

        Returns:
            list: A list containing the details of the added persons.
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
        """Return the details of added persons from the web table.

        Returns:
            list: A list containing the added persons details.
        """
        person_list = self.elements_are_present(self.locators.FULL_PERSONS_LIST)
        data = []
        for item in person_list:
            data.append(item.text.splitlines())
        return data

    def search_person(self, keyword):
        """Search person with keyword.

        Args:
            keyword (str): The keyword to search for.
        """
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(keyword)

    def check_search_person(self):
        """Check and return data about a person in a table row.

        Returns:
            list: A list with the person's data from the table row.
        """
        # Finding person data with DELETE_BUTTON parent element by XPATH
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        parent_row = delete_button.find_element(*self.locators.PARENT_ROW)
        return parent_row.text.splitlines()

    def edit_person_info(self):
        """Edit person random data field and return edited data.

        Returns:
            str: Edited data.
        """
        # Generating new person age data
        person_info = next(generate_person())
        # Selecting random person data field and getting its value
        random_field = random.choice(list(vars(person_info).keys()))
        data_to_edit = getattr(person_info, random_field)
        # Defining needed field locator
        fields_locators = {
            'first_name': self.locators.FIRST_NAME_INPUT,
            'last_name': self.locators.LAST_NAME_INPUT,
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
        """Delete a person's entry from the table."""
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted_person(self):
        """Check and return the deletion of a person's entry from the table.

        Returns:
            str: Text of the label indicating no rows are found.
        """
        return self.element_is_present(self.locators.NO_ROWS_FOUND_LABEL).text

    def change_displayed_rows_count(self):
        """Change the number of rows displayed per page and return the row count for each setting.

        Returns:
            list: A list of actual row counts displayed for each setting.
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
        """Check the number of rows currently displayed on the page.

        Returns:
            int: The number of rows currently displayed on the page.
        """
        list_rows = self.elements_are_present(self.locators.FULL_PERSONS_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):  # https://demoqa.com/buttons
    locators = ButtonsLocators()

    def click_double_button(self):
        """Perform double-click action on the button and return output text.

        Returns:
            str: The output text after the double-click action.
        """
        self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_BUTTON))
        return self.check_clicked_buttons(self.locators.DOUBLE_CLICK_OUTPUT_RESULT)

    def click_right_button(self):
        """Perform a right-click action on the right-click button and return the result.

        Returns:
            str: The output text after the right-click action.
        """
        self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
        return self.check_clicked_buttons(self.locators.RIGHT_CLICK_OUTPUT_RESULT)

    def click_dynamic_button(self):
        """Perform a click action on the dynamically loaded button and return the result.

        Returns:
            str: The result text after the click action.
        """
        self.element_is_visible(self.locators.LEFT_CLICK_BUTTON).click()
        return self.check_clicked_buttons(self.locators.LEFT_CLICK_OUTPUT_RESULT)

    def check_clicked_buttons(self, element):
        """Check the result of the click actions by getting the text of the specified element.

        Args:
            element (WebElement): The locator of the element to check output result.

        Returns:
            str: The text of the output for the element.
        """
        return self.element_is_present(element).text


class LinksPage(BasePage):  # https://demoqa.com/links
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        """Check if a simple link opens in a new tab and returns the URL.

        Returns:
            tuple: A tuple containing the href of the link and the URL of the new tab, or an error message and None.
        """
        try:  # Locate the simple link element
            simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        except Exception as e:
            return f"Error locating simple link: {str(e)}.", None

        link_href = simple_link.get_attribute('href')
        try:  # Send a request to the link URL
            request = requests.get(link_href)
            request.raise_for_status()
        except requests.RequestException as e:
            return f"Error requesting simple link: {str(e)}.", None

        try:
            # Click and open new tab
            simple_link.click()
            # Switch to new tab with handle 1
            self.driver.switch_to.window(self.driver.window_handles[1])
            # Get the current tab url
            url = self.driver.current_url
            return link_href, url
        except TimeoutException:
            return link_href, "Error: new tab did not open in time."
        except Exception as e:
            return link_href, f"Error: {str(e)}."

    def check_new_tab_dynamic_link(self):
        """Check if a dynamic link opens in a new tab and returns the URL.

        Returns:
            tuple: A tuple containing the href of the link and the URL of the new tab, or an error message and None.
        """
        try:  # Locate the simple link element
            dynamic_link = self.element_is_visible(self.locators.DYNAMIC_LINK)
        except Exception as e:
            return f"Error locating dynamic link: {str(e)}.", None

        link_href = dynamic_link.get_attribute('href')
        try:  # Send a request to the link URL
            request = requests.get(link_href)
            request.raise_for_status()
        except requests.RequestException as e:
            return f"Error requesting simple link: {str(e)}.", None

        try:
            # Click and open new tab
            dynamic_link.click()
            # Switch to new tab with handle 1
            self.driver.switch_to.window(self.driver.window_handles[1])
            # Get the current tab url
            url = self.driver.current_url
            return link_href, url
        except TimeoutException:
            return link_href, "Error: new tab did not open in time."
        except Exception as e:
            return link_href, f"Error: {str(e)}."

    def get_link_output_response(self, code, status_text):
        """Check if the output text contains the specified status code and status message.

        Args:
            code (int): The status code to check in the output text.
            status_text (str): The status message to check in the output text.

        Returns:
            bool: True if both the status code and status message are found in the output text, otherwise False.
        """
        output_text = self.element_is_present(self.locators.LINK_RESPONSE_OUTPUT_RESULT).text
        if str(code) in output_text and status_text in output_text:
            return True
        else:
            return False

    def check_apicall_link(self, url, expected_code):
        """Check if a link returns the expected status code and click the corresponding link element.

    Args:
        url (str): The URL to send the request to.
        expected_code (int): The expected status code of the response.

    Returns:
        int: The status code of the response.
        str: Error message if clicking the link element fails.
        """
        buttons = {201: self.locators.CREATED_LINK,
                   301: self.locators.MOVED_LINK,
                   400: self.locators.BAD_REQUEST_LINK,
                   401: self.locators.UNAUTHORIZED_LINK,
                   403: self.locators.FORBIDDEN_LINK,
                   404: self.locators.NOTFOUND_LINK}
        request = requests.get(url)
        if request.status_code == expected_code:
            try:
                self.element_is_present(buttons[expected_code]).click()
            except Exception as e:
                return f"Error clicking link: {str(e)}."
        return request.status_code


class UploadDownloadPage(BasePage):
    """Upload and Download Page."""
    locators = UploadDownloadPageLocators()

    def upload_file(self):
        """Generate a file, upload it, and check the uploaded result.

        Returns:
            tuple: A tuple containing the filename and the name of the uploaded file from page.
        """
        filename, path = generate_file()  # Create file
        self.element_is_present(self.locators.UPLOAD_INPUT).send_keys(str(path))  # Upload file
        os.remove(path)  # Delete file
        result = self.element_is_present(self.locators.UPLOADED_RESULT).text
        # Convert path strings to Path objects
        filename_path = Path(filename).resolve()
        result_path = Path(result).resolve()
        return filename_path.name, result_path.name

    def download_file(self):
        """"""

        pass
