from selenium.webdriver.common.by import By  # By class for locating elements


class TextBoxLocators:  # Class to hold locator constants for the TextBox page
    # Form fields to be filled in
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")
    # Created form data
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxLocators:  # Class to hold locator constants for the CheckBox page
    # Form fields to be filled in
    EXPAND_ALL = (By.CSS_SELECTOR, "button[title='Expand All']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    # Created form data
