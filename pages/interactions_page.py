import time
import random

from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    """https://demoqa.com/accordian"""
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        """Returns a list of text from all sortable items specified by the elements locator.

        Args:
            elements (tuple): Locator tuple for the sortable items.

        Returns:
            list: A list of text from each sortable item.
        """
        items = self.elements_are_visible(elements)
        return [item.text for item in items]

    def switch_two_elements(self, element):
        """Switch to a specified sortable tab (list or grid), shuffle two items within the tab,
        and return their order before and after the shuffle.

        Args:
            element (str): Specifies which tab to switch to ('list' or 'grid').

        Returns:
            tuple: A tuple containing two lists, representing the order of items before and after the shuffle.
        """
        sortable_locators = {
            "list": {
                "tab": self.locators.LIST_TAB_A,
                "items": self.locators.LIST_ITEMS
            },
            "grid": {
                "tab": self.locators.GRID_TAB_A,
                "items": self.locators.GRID_ITEMS
            },
        }
        # Switch to tab
        self.element_is_visible(sortable_locators[element]["tab"]).click()
        order_before = self.get_sortable_items(sortable_locators[element]["items"])
        # Shuffle two items
        items_to_shuffle = random.sample(self.elements_are_visible(sortable_locators[element]["items"]), k=2)
        source, target = items_to_shuffle[0], items_to_shuffle[1]
        self.action_drag_and_drop_to_element(source, target)

        order_after = self.get_sortable_items(sortable_locators[element]["items"])
        return order_before, order_after


class SelectablePage(BasePage):
    """https://demoqa.com/selectable"""
    locators = SelectablePageLocators()

    def click_random_selectable_item(self, elements):
        """Clicks on a random selectable item from the list of elements.

        Args:
            elements (tuple): Locator tuple for the selectable items.
        """
        items = self.elements_are_visible(elements)
        random.sample(items, k=1)[0].click()
        pass

    def get_selectable_items(self, element):
        """Switches to a specified selectable tab (list or grid), randomly selects a number of items,
        and returns the count of selected items and the list of active (selected) items.

        Args:
            element (str): Specifies which tab to switch to ('list' or 'grid').

        Returns:
            tuple: A tuple containing the count of selected items and a list of active (selected) items.
        """
        selectable_locators = {
            "list": {
                "tab": self.locators.LIST_TAB_A,
                "items": self.locators.LIST_ITEMS,
                "active_items": self.locators.LIST_ITEMS_ACTIVE,
            },
            "grid": {
                "tab": self.locators.GRID_TAB_A,
                "items": self.locators.GRID_ITEMS,
                "active_items": self.locators.GRID_ITEMS_ACTIVE,
            },
        }

        self.element_is_visible(selectable_locators[element]["tab"]).click()
        count = random.randint(1, len(selectable_locators[element]["items"]))
        for i in range(count):
            self.click_random_selectable_item(selectable_locators[element]["items"])
        active_elements = self.elements_are_visible(selectable_locators[element]["active_items"])
        return count, active_elements


class ResizablePage(BasePage):
    """https://demoqa.com/resizable"""
    locators = ResizablePageLocators()

    def get_size_values(self, size):
        """Extracts the width and height values from a CSS style string.

        Args:
            size (str): CSS style string containing size information.

        Returns:
            tuple: A tuple containing the width and height as strings.
        """
        width = size.split(';')[0].split(':')[1].replace(' ', '')
        height = size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_minmax_size(self, element):
        """Retrieves the style attribute value of the specified element.

        Args:
            element (tuple): Locator tuple for the element.

        Returns:
            str: The style attribute value of the element.
        """
        size = self.element_is_present(element)
        size_style = size.get_attribute("style")
        return size_style

    def change_resizable_size(self, element):
        """Resizes the specified resizable element by increasing and then decreasing its size.

        Args:
            element (str): Specifies which resizable element to interact with ('constraint' or 'resizable').

        Returns:
            tuple: A tuple containing the maximum and minimum size values as two separate tuples.
        """
        resizable_locators = {
            "constraint": {
                "box": self.locators.RESIZABLE_CONSTRAINT,
                "handle": self.locators.RESIZABLE_CONSTRAINT_HANDLE,
                "max": (400, 200),
                "min": (-400, -200),
            },
            "resizable": {
                "box": self.locators.RESIZABLE,
                "handle": self.locators.RESIZABLE_HANDLE,
                "max": (random.randint(1, 200), random.randint(1, 200)),
                "min": (random.randint(-200, -1), random.randint(-200, -1)),
            },
        }
        # Increase size
        self.go_to_element(self.element_is_present(resizable_locators[element]['handle']))
        self.action_drag_and_drop_by_offset(self.element_is_present(resizable_locators[element]['handle']),
                                            resizable_locators[element]['max'][0],
                                            resizable_locators[element]['max'][1])
        self.go_to_element(self.element_is_present(resizable_locators[element]['box']))
        max_size = self.get_size_values(self.get_minmax_size(resizable_locators[element]['box']))
        # Decrease size
        self.action_drag_and_drop_by_offset(self.element_is_present(resizable_locators[element]['handle']),
                                            resizable_locators[element]['min'][0],
                                            resizable_locators[element]['min'][1])
        min_size = self.get_size_values(self.get_minmax_size(resizable_locators[element]['box']))

        return max_size, min_size

