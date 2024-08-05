from selenium.webdriver.common.by import By


class SortablePageLocators:
    # Tabs
    LIST_TAB_A = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    GRID_TAB_A = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    # Items
    LIST_ITEMS = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] '
                                   'div[class="list-group-item list-group-item-action"]')
    GRID_ITEMS = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] '
                                   'div[class="list-group-item list-group-item-action"]')


class SelectablePageLocators:
    # Tabs
    LIST_TAB_A = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    GRID_TAB_A = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    # List items
    LIST_ITEMS = (By.CSS_SELECTOR, 'ul[id="verticalListContainer"] '
                                   'li[class="mt-2 list-group-item list-group-item-action"]')
    LIST_ITEMS_ACTIVE = (By.CSS_SELECTOR, 'ul[id="verticalListContainer"] '
                                          'li[class="mt-2 list-group-item active list-group-item-action"]')
    # Grid items
    GRID_ITEMS = (By.CSS_SELECTOR, 'div[id="gridContainer"] '
                                   'li[class="list-group-item list-group-item-action"]')
    GRID_ITEMS_ACTIVE = (By.CSS_SELECTOR, 'div[id="gridContainer"] '
                                          'li[class="list-group-item active list-group-item-action"]')


class ResizablePageLocators:
    # Tabs
    RESIZABLE_CONSTRAINT = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    RESIZABLE_CONSTRAINT_HANDLE = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"] '
                                                    'span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE = (By.CSS_SELECTOR, 'div[id="resizable"]')
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, 'div[id="resizable"] '
                                         'span[class="react-resizable-handle react-resizable-handle-se"]')
