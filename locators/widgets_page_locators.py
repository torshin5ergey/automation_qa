from selenium.webdriver.common.by import By


class AccordianPageLocators:
    # First section WHAT
    FIRST_SECTION_HEADER = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    FIRST_SECTION_TEXT = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    # Second section WHERE
    SECOND_SECTION_HEADER = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECOND_SECTION_TEXT = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    # Third section WHY
    THIRD_SECTION_HEADER = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    THIRD_SECTION_TEXT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutocompletePageLocators:
    # Multiple
    MULTI_COMPLETE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_COMPLETE_VALUES = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_COMPLETE_VALUE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    # Single
    SINGLE_COMPLETE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    SINGLE_COMPLETE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')

