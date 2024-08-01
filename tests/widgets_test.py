import random
import time

import generator.generator
from conftest import driver
from pages.widgets_page import AccordianPage, AutocompletePage, DatePickerPage, SliderPage


class TestWidgets:

    class TestAccordian:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()

            first_header, first_text = accordian_page.get_section_data(1)
            second_header, second_text = accordian_page.get_section_data(2)
            third_header, third_text = accordian_page.get_section_data(3)
            assert first_header == 'What is Lorem Ipsum?' and len(first_text) > 0, "Error. First section has not opened."
            assert second_header == 'Where does it come from?' and len(second_text) > 0, "Error. Second section has not opened."
            assert third_header == 'Why do we use it?' and len(third_text) > 0, "Error. Third section has not opened."


class TestAutoComplete:
    def test_autocomplete_multi(self, driver, generate_color=None):
        autocomplete_page = AutocompletePage(driver, "https://demoqa.com/auto-complete")
        autocomplete_page.open()
        
        colors_count = random.randint(1, 11)
        selected_colors = autocomplete_page.add_value_multi(num=colors_count)
        result_colors = autocomplete_page.get_current_multi_selection()
        assert selected_colors == result_colors, "Error. Selected colors are missing in the input."

    def test_remove_value_multi(self, driver):
        autocomplete_page = AutocompletePage(driver, "https://demoqa.com/auto-complete")
        autocomplete_page.open()

        colors_count = random.randint(2, 11)
        autocomplete_page.add_value_multi(num=colors_count)
        before, after = autocomplete_page.remove_value_multi(num=colors_count-1)
        assert after == 1 and before != after, "Error. Values has not been deleted from input."

    def test_clear_values_multi(self, driver):
        autocomplete_page = AutocompletePage(driver, "https://demoqa.com/auto-complete")
        autocomplete_page.open()

        colors_count = random.randint(1, 11)
        selected_colors = autocomplete_page.add_value_multi(num=colors_count)
        autocomplete_page.clear_all_multi()
        result_colors = autocomplete_page.get_current_multi_selection()
        assert len(selected_colors) != 0 and len(result_colors) == 0, "Error. The values has not been cleared."

    def test_autocomplete_single(self, driver):
        autocomplete_page = AutocompletePage(driver, "https://demoqa.com/auto-complete")
        autocomplete_page.open()

        selected_color = autocomplete_page.add_value_single()
        result_color = autocomplete_page.get_current_single_selection()
        assert selected_color == result_color, "Error. Selected color is missing in the input."


class TestDatePicker:
    def test_select_date(self, driver):
        datepicker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
        datepicker_page.open()

        before, after = datepicker_page.set_date()
        assert before != after, "Error. Date has not been changed."

    def test_select_datetime(self, driver):
        datepicker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
        datepicker_page.open()

        before, after = datepicker_page.set_datetime()
        assert before != after, "Error. Date and time has not been changed."

class TestSlider:
    def test_change_slider_value(self, driver):
        slider_page = SliderPage(driver, "https://demoqa.com/slider")
        slider_page.open()

        before, after = slider_page.change_slider_value()
        print(before, after)
