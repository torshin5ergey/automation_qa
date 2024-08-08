from selenium.webdriver.common.by import By


class SortablePageLocators:
    # Tabs
    LIST_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    GRID_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    # Items
    LIST_ITEMS = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] '
                                   'div[class="list-group-item list-group-item-action"]')
    GRID_ITEMS = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] '
                                   'div[class="list-group-item list-group-item-action"]')


class SelectablePageLocators:
    # Tabs
    LIST_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    GRID_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
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


class DroppablePageLocators:
    # Simple
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-simple"]')
    SIMPLE_DRAGGABLE = (By.CSS_SELECTOR, '#simpleDropContainer #draggable')
    SIMPLE_DROPPABLE = (By.CSS_SELECTOR, '#simpleDropContainer #droppable')

    # Accept
    ACCEPT_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
    ACCEPT_ACCEPTABLE_DRAGGABLE = (By.CSS_SELECTOR, 'div[id="acceptDropContainer"] '
                                                    'div[id="acceptable"]')
    ACCEPT_NOT_ACCEPTABLE_DRAGGABLE = (By.CSS_SELECTOR, 'div[id="acceptDropContainer"] '
                                                        'div[id="notAcceptable"]')
    ACCEPT_DROPPABLE = (By.CSS_SELECTOR, 'div[id="acceptDropContainer"] '
                                         'div[id="droppable"]')

    # Prevent Propogation
    PREV_PROP_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-preventPropogation"]')
    PREV_PROP_DRAGGABLE = (By.CSS_SELECTOR, 'div[id="dragBox"]')
    # Not greedy outer
    NOT_GREEDY_OUTER_DROPPABLE = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"]')
    NOT_GREEDY_OUTER_DROPPABLE_TEXT = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"] '
                                                        'p:nth-child(1)')
    # Not greedy inner
    NOT_GREEDY_INNER_DROPPABLE = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    NOT_GREEDY_INNER_DROPPABLE_TEXT = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"] '
                                                        'p:nth-child(1)')
    # Greedy outer
    GREEDY_OUTER_DROPPABLE = (By.CSS_SELECTOR, 'div[id="greedyDropBox"]')
    GREEDY_OUTER_DROPPABLE_TEXT = (By.CSS_SELECTOR, 'div[id="greedyDropBox"] '
                                                    'p:nth-child(1)')
    # Greedy inner
    GREEDY_INNER_DROPPABLE = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]')
    GREEDY_INNER_DROPPABLE_TEXT = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"] '
                                                    'p:nth-child(1)')

    # Revert Draggable
    REV_DRAG_TAB = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-revertable"]')
    REV_GRAG_WILL_REVERT = (By.CSS_SELECTOR, 'div[id="revertableDropContainer"] '
                                             'div[id="revertable"]')
    REV_GRAG_NOT_REVERT = (By.CSS_SELECTOR, 'div[id="revertableDropContainer"] '
                                            'div[id="notRevertable"]')
    REV_DRAG_DROPPABLE = (By.CSS_SELECTOR, 'div[id="revertableDropContainer"] div[id="droppable"]')
