import allure

from conftest import driver
from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


@allure.suite("Interactions section")
class TestInteractions:
    @allure.feature("Sortable page")
    class TestSortable:
        @allure.title("Test sortable list")
        def test_sortable_list(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()

            before, after = sortable_page.switch_two_elements("list")
            assert before != after, "Error. List elements have not been sorted."

        @allure.title("Test sortable grid")
        def test_sortable_grid(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()

            before, after = sortable_page.switch_two_elements("grid")
            assert before != after, "Error. Grid elements have not been sorted."

    @allure.feature("Selectable page")
    class TestSelectable:
        @allure.title("Test selectable list")
        def test_selectable_list(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()

            count, active = selectable_page.get_selectable_items("list")
            assert count == len(active), "Error. List elements have not been selected."

        @allure.title("Test selectable grid")
        def test_selectable_grid(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()

            count, active = selectable_page.get_selectable_items("grid")
            assert count == len(active), "Error. Grid elements have not been selected."

    @allure.feature("Resizable page")
    class TestResizable:
        @allure.title("Test resizable constraints")
        def test_resizable_constraints(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()

            max_size, min_size = resizable_page.change_resizable_size("constraint")
            assert ('500px', '300px') == max_size, "Error. Maximum size is noq equal to 500x300."
            assert ('150px', '150px') == min_size, "Error. Minimum size is noq equal to 150x150."

        @allure.title("Test resizable")
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()

            max_size, min_size = resizable_page.change_resizable_size("resizable")
            assert min_size != max_size, "Error. Resizable box size has not been changed."

    @allure.feature("Droppable page")
    class TestDroppable:
        @allure.title("Test Simple")
        def test_simple(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()

            text = droppable_page.drop_simple()
            assert text == "Dropped!", "Error. The simple element has not been dropped."

        @allure.title("Test Accept")
        def test_accept(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()

            not_acc_text, acc_text = droppable_page.drop_accept()
            assert not_acc_text == "Drop here", "Error. Not Acceptable element has been accepted."
            assert acc_text == "Dropped!", "Error. Acceptable element has not been accepted."

        @allure.title("Test Prevent Propagation, not greedy")
        def test_prevent_propagation_not_greedy(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()

            inner_text, outer_text = droppable_page.drop_prevent_propagation("not_greedy")
            assert inner_text == "Dropped!", "Error. The inner box hasn't been changed its text."
            assert outer_text == "Dropped!", "Error. The outer box has been changed its text."

        @allure.title("Test Prevent Propagation, greedy")
        def test_prevent_propagation_greedy(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()

            inner_text, outer_text = droppable_page.drop_prevent_propagation("greedy")
            assert inner_text == "Dropped!", "Error. The inner box hasn't been changed its text."
            assert outer_text == "Outer droppable", "Error. The outer box has been changed its text."

        @allure.title("Test Revert Draggable, will revert")
        def test_will_revert_draggable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()

            after_move, after_revert = droppable_page.drop_revert_draggable("will_revert")
            assert after_move != after_revert

        @allure.title("Test Revert Draggable, not revert")
        def test_not_revert_draggable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()

            after_move, after_revert = droppable_page.drop_revert_draggable("not_revert")
            assert after_move == after_revert

    @allure.feature("Draggable page")
    class TestDraggable:
        @allure.title("Test Simple")
        def test_simple(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()

            before, after = draggable_page.drag_simple()
            assert before != after, "Error. Simple dragbox position has not been changed."

        @allure.title("Test Axis Restricted, only X")
        def test_axis_restricted_only_x(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()

            before, after = draggable_page.drag_axis_restricted('x')
            assert before[0] == after[0] and before[1] != after[1], ("Error. X axis restricted dragbox position has "
                                                                     "been changed incorrectly.")

        @allure.title("Test Axis Restricted, only Y")
        def test_axis_restricted_only_y(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()

            before, after = draggable_page.drag_axis_restricted('y')
            assert before[0] != after[0] and before[1] == after[1], ("Error. Y axis restricted dragbox position has "
                                                                     "been changed incorrectly.")

        # TODO: Container restricted
