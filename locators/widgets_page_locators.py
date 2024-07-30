from selenium.webdriver.common.by import By


class AccordianPageLocators:
    # First section WHAT
    FIRST_SECTION_HEADER = (By.CSS_SELECTOR, 'div[id=section1Heading]')
    FIRST_SECTION_TEXT = (By.CSS_SELECTOR, 'div[id=section1Content] p')
    # Second section WHERE
    SECOND_SECTION_HEADER = (By.CSS_SELECTOR, 'div[id=section2Heading]')
    SECOND_SECTION_TEXT = (By.CSS_SELECTOR, 'div[id=section2Content] p')
    # Third section WHY
    THIRD_SECTION_HEADER = (By.CSS_SELECTOR, 'div[id=section3Heading]')
    THIRD_SECTION_TEXT = (By.CSS_SELECTOR, 'div[id=section3Content] p')
