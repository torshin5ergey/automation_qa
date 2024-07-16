import os
import time

from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.forms_page_locators import FormsPageLocators
from generator.generator import generate_person, generate_file


class FormsPage(BasePage):
    """Practice Form Page https://demoqa.com/automation-practice-form"""
    locators = FormsPageLocators()

    def fill_form_fields(self):
        """
        Fills out the form fields with generated mock person data and submits the form.

        Returns:
            list: A list containing formatted person data (full name, email, current address, phone).
        """
        person = next(generate_person())
        filename, path = generate_file('jpg')
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER_RADIO_RADIO).click()
        self.element_is_visible(self.locators.MOBILE_INPUT).send_keys(person.phone)
        self.element_is_visible(self.locators.SUBJECTS_INPUT).send_keys("Maths")
        self.element_is_visible(self.locators.SUBJECTS_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES_CHECKBOX).click()
        self.element_is_present(self.locators.PICTURE_FILE_INPUT).send_keys(str(path))
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS_TEXTAREA).send_keys(person.current_address)
        self.go_to_element(self.element_is_present(self.locators.SELECT_STATE_DIV))
        self.element_is_visible(self.locators.SELECT_STATE_DIV).click()
        self.element_is_visible(self.locators.SELECT_STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_CITY_DIV).click()
        self.element_is_visible(self.locators.SELECT_CITY_INPUT).send_keys(Keys.RETURN)
        self.go_to_element(self.element_is_present(self.locators.SUBMIT_BUTTON))
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()

        # Format person data
        output_data = [
            f"{person.first_name} {person.last_name}",
            person.email,
            person.current_address,
            person.phone[:10]
        ]
        return output_data

    def get_form_result(self):
        """
        Retrieves the form result data from the results table.

        Returns:
            list: A list of strings, each containing text from the results table.
        """
        result_list = self.elements_are_present(self.locators.RESULT_TABLE_VALUES)
        data = []
        for i in result_list:
            self.go_to_element(i)
            data.append(i.text)
        return data
