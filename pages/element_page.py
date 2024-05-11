import time

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
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):  # CheckBox page, inheriting from BasePage
    locators = CheckBoxLocators  # Setting locators attribute to CheckLocators class for element locators
