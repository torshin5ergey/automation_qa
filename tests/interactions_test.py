from conftest import driver
from pages.interactions_page import SortablePage


class TestInteractions:

    class TestSortable:
        def test_sortable_list(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()

            before, after = sortable_page.switch_two_elements("list")
            assert before != after, "Error. List elements did not sorted."

        def test_sortable_grid(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()

            before, after = sortable_page.switch_two_elements("grid")
            assert before != after, "Error. Grid elements did not sorted."
