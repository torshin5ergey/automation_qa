import time
import random

from locators.interactions_page_locators import SortablePageLocators
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
        sorted_locators = {
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
        self.element_is_visible(sorted_locators[element]["tab"]).click()
        order_before = self.get_sortable_items(sorted_locators[element]["items"])
        # Shuffle two items
        items_to_shuffle = random.sample(self.elements_are_visible(sorted_locators[element]["items"]), k=2)
        source, target = items_to_shuffle[0], items_to_shuffle[1]
        self.action_drag_and_drop_to_element(source, target)

        order_after = self.get_sortable_items(sorted_locators[element]["items"])
        return order_before, order_after
