import random
import time

from pages.base_page import BasePage
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage
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
            assert output_yes == 'yes', "'Yes' have not been selected"
            assert output_impressive == 'impressive', "'Impressive' have not been selected"
            assert output_no == 'no', "'No' have not been selected"

    class TestWebTable:  # WebTable Page functionality
        def test_webtable_add_person(self, driver):
            # Creating an instance of the WebTablePage class with the WebDriver instance and checkbox URL
            webtable_page = WebTablePage(driver, "https://demoqa.com/webtables")
            # Opening the URL in the browser
            webtable_page.open()
            new_person = webtable_page.add_new_person()
            table_result = webtable_page.check_added_person()
            assert new_person in table_result, "The person was not added in the table"

        def test_webtable_search_person(self, driver):
            # Creating an instance of the WebTablePage class with the WebDriver instance and checkbox URL
            webtable_page = WebTablePage(driver, "https://demoqa.com/webtables")
            # Opening the URL in the browser
            webtable_page.open()
            new_person_keyword = webtable_page.add_new_person()[random.randint(0, 5)]
            webtable_page.search_person(new_person_keyword)
            table_result = webtable_page.check_search_person()
            assert new_person_keyword in table_result, "The person was not found in the table."

        def test_webtable_edit_person(self, driver):
            # Creating an instance of the WebTablePage class with the WebDriver instance and checkbox URL
            webtable_page = WebTablePage(driver, "https://demoqa.com/webtables")
            # Opening the URL in the browser
            webtable_page.open()
            # Generating new person and get his lastname
            lastname = webtable_page.add_new_person()[1]
            # Search added person by lastname
            webtable_page.search_person(lastname)
            edited_data = webtable_page.edit_person_info()
            row = webtable_page.check_search_person()
            assert edited_data in row, "The person data has not been changed."

        def test_webtable_delete_person(self, driver):
            # Creating an instance of the WebTablePage class with the WebDriver instance and checkbox URL
            webtable_page = WebTablePage(driver, "https://demoqa.com/webtables")
            # Opening the URL in the browser
            webtable_page.open()
            # Generating new person and get his lastname
            email = webtable_page.add_new_person()[3]
            webtable_page.search_person(email)
            webtable_page.delete_person()
            text = webtable_page.check_deleted_person()
            assert text == "No rows found"

        def test_webtable_change_rows_per_page(self, driver):
            # Creating an instance of the WebTablePage class with the WebDriver instance and checkbox URL
            webtable_page = WebTablePage(driver, "https://demoqa.com/webtables")
            # Opening the URL in the browser
            webtable_page.open()
            count = webtable_page.change_displayed_rows_count()
            assert count == [5, 10, 20, 25, 50, 100], ("The rows per page number has not been changed or has changed incorrectly.")

    class TestButtonsPage:  # Click, Double-click, Right-click Page functionality
        def test_buttons_clicks(self, driver):
            # Creating an instance of the ButtonsPage class with the WebDriver instance and checkbox URL
            buttons_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            # Opening the URL in the browser
            buttons_page.open()
            double = buttons_page.click_double_button()
            right = buttons_page.click_right_button()
            left = buttons_page.click_dynamic_button()
            assert double == "You have done a double click", "The double click button was not pressed."
            assert right == "You have done a right click", "The right click button was not pressed."
            assert left == "You have done a dynamic click", "The dynamic click button was not pressed."

