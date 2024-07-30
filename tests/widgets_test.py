from conftest import driver
from pages.widgets_page import AccordianPage


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
