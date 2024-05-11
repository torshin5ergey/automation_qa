import time

from pages.base_page import BasePage
from pages.element_page import TextBoxPage, CheckBoxPage
from conftest import driver  # Importing the WebDriver instance as a fixture


class TestElements:
    class TestTextBox:  # TextBoxPage functionality
        def test_textbox(self, driver):
            # Creating an instance of the TextBoxPage class with the WebDriver instance and textbox URL
            textbox_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            # Opening the URL in the browser
            textbox_page.open()

            # Fill all fields
            full_name, email, current_address, permanent_address = textbox_page.fill_all_fields()
            # Check filled data
            output_full_name, output_email, output_cur_address, output_perm_address = textbox_page.check_filled_form()
            # Assert all fields
            assert full_name == output_full_name, "the fullname does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_cur_address, "the current address does not match"
            assert permanent_address == output_perm_address, "the permanent address does not match"

    class TestCheckBox:  # CheckBoxPage functionality
        def test_checkbox(self, driver):
            # Creating an instance of the CheckPage class with the WebDriver instance and checkbox URL
            checkbox_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            # Opening the URL in the browser
            checkbox_page.open()
