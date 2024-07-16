import random

from selenium.webdriver.common.by import By


class FormsPageLocators:
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    GENDER_RADIO_RADIO = (By.CSS_SELECTOR, f"div[class*='custom-control'] "
                                           f"label[for='gender-radio-{random.randint(1, 3)}']")
    MOBILE_INPUT = (By.CSS_SELECTOR, "input[id='userNumber']")
    DATE_OF_BIRTH_INPUT = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    SUBJECTS_INPUT = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    SUBJECTS_LIST = (By.CSS_SELECTOR, ".subjects-auto-complete__option")
    HOBBIES_CHECKBOX = (By.CSS_SELECTOR, f"div[class*='custom-control'] "
                                         f"label[for='hobbies-checkbox-{random.randint(1, 3)}']")
    PICTURE_FILE_INPUT = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    CURRENT_ADDRESS_TEXTAREA = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    SELECT_STATE_DIV = (By.CSS_SELECTOR, "div[id='state']")
    SELECT_STATE_INPUT = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    SELECT_CITY_DIV = (By.CSS_SELECTOR, "div[id='city']")
    SELECT_CITY_INPUT = (By.CSS_SELECTOR, "input[id='react-select-4-input']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")
    # Result popup table
    RESULT_TABLE_LABELS = (By.XPATH, "//div[@class='table-responsive']//td[1]")
    RESULT_TABLE_VALUES = (By.XPATH, "//div[@class='table-responsive']//td[2]")
