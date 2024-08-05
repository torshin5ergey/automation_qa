from conftest import driver
from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


class TestInteractions:

    class TestSortable:
        def test_sortable_list(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()

            before, after = sortable_page.switch_two_elements("list")
            assert before != after, "Error. List elements have not been sorted."

        def test_sortable_grid(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()

            before, after = sortable_page.switch_two_elements("grid")
            assert before != after, "Error. Grid elements have not been sorted."

    class TestSelectable:
        def test_selectable_list(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()

            count, active = selectable_page.get_selectable_items("list")
            assert count == len(active), "Error. List elements have not been selected."

        def test_selectable_grid(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()

            count, active = selectable_page.get_selectable_items("grid")
            assert count == len(active), "Error. Grid elements have not been selected."

    class TestResizable:
        def test_resizable_constraints(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()

            max_size, min_size = resizable_page.change_resizable_size("constraint")
            assert ('500px', '300px') == max_size, "Error. Maximum size is noq equal to 500x300."
            assert ('150px', '150px') == min_size, "Error. Minimum size is noq equal to 150x150."

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()

            max_size, min_size = resizable_page.change_resizable_size("resizable")
            assert min_size != max_size, "Error. Resizable box size has not been changed."
