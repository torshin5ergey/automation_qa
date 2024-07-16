import time

from conftest import driver
from pages.forms_page import FormsPage


class TestForms:

    class TestFormsPage:
        def test_forms(self, driver):
            forms_page = FormsPage(driver, "https://demoqa.com/automation-practice-form")
            forms_page.open()

            person_data = forms_page.fill_form_fields()
            result_data = forms_page.get_form_result()

            assert person_data == [
                result_data[0],  # Student Name
                result_data[1],  # Student Email
                result_data[8],  # Address
                result_data[3],  # Mobile
                                   ], "Error: The form has not been filled."
