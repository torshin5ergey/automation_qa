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
    MULTI_CLEAR_VALUES = (By.CSS_SELECTOR, 'div[class="auto-complete__indicator auto-complete__clear-indicator css-tlfecz-indicatorContainer"] svg path')
    # Single
    SINGLE_COMPLETE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    SINGLE_COMPLETE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')


class DatePickerPageLocators:
    # Date
    DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATE_SELECT_DAY = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')
    # Datetime
    DATETIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATETIME_SELECT_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATETIME_SELECT_YEAR_LIST = (By.CSS_SELECTOR, '[class="react-datepicker__year-option"]')
    DATETIME_SELECT_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATETIME_SELECT_MONTH_LIST = (By.CSS_SELECTOR, '[class="react-datepicker__month-option"]')
    DATETIME_SELECT_TIME_LIST = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')
    DATETIME_SELECT_DAY = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day--"]')

