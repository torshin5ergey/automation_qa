import time

from pages.base_page import BasePage
from pages.element_page import TextBoxPage, CheckBoxPage, RadioButtonPage
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
            assert full_name == output_full_name, "The fullname does not match"
            assert email == output_email, "The email does not match"
            assert current_address == output_cur_address, "The current address does not match"
            assert permanent_address == output_perm_address, "The permanent address does not match"

    class TestCheckBox:  # CheckBoxPage functionality
        def test_checkbox(self, driver):
            # Creating an instance of the CheckBoxPage class with the WebDriver instance and checkbox URL
            checkbox_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            # Opening the URL in the browser
            checkbox_page.open()

            # Toggle all items
            checkbox_page.open_full_list()
            checkbox_page.click_random_checkbox()
            input_checkboxes = checkbox_page.get_checked_checkboxes()
            output_result = checkbox_page.get_output_result()
            # Assert result
            assert input_checkboxes == output_result, "The checkboxes have not been selected"

    class TestRadioButton:  # RadioButton Page functionality
        def test_radiobutton(self, driver):
            # Creating an instance of the RadioButtonPage class with the WebDriver instance and checkbox URL
            radiobutton_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            # Opening the URL in the browser
            radiobutton_page.open()
            radiobutton_page.click_radio('yes')
            output_yes = radiobutton_page.get_output_result()
            radiobutton_page.click_radio('impressive')
            output_impressive = radiobutton_page.get_output_result()
            radiobutton_page.click_radio('no')
            output_no = radiobutton_page.get_output_result()
            # Assert results
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == 'No', "'No' have not been selected"

