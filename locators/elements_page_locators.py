from selenium.webdriver.common.by import By  # By class for locating elements


class TextBoxLocators:  # Locator constants for the TextBox page
    # Form fields to be filled in
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")
    # Created form data
    OUTPUT_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    OUTPUT_EMAIL = (By.CSS_SELECTOR, "#output #email")
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxLocators:  # Locator constants for the CheckBox page
    # Form fields to be filled in
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    # Checked data
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    ITEM_TITLE = (By.XPATH, ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonLocators:  # Locator constants for the RadioButton page
    RADIO_YES = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    RADIO_IMPRESSIVE = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    RADIO_NO = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")


class WebTableLocators:  # Locator constants for the WebTable page
    # Add person form
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")
    # Table
    FULL_PERSONS_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    PARENT_ROW = (By.XPATH, ".//ancestor::div[@class='rt-tr-group']")
    NO_ROWS_FOUND_LABEL = (By.CSS_SELECTOR, "div[class='rt-noData']")
    ROWS_PER_PAGE_SELECT = (By.CSS_SELECTOR, "select[aria-label='rows per page']")
    # Edit person form
    UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")


class ButtonsLocators:  # Locator constants for the Buttons page
    # Buttons
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    LEFT_CLICK_BUTTON = (By.XPATH, "//button[text()='Click Me']")
    # Output labels
    DOUBLE_CLICK_OUTPUT_RESULT = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    RIGHT_CLICK_OUTPUT_RESULT = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    LEFT_CLICK_OUTPUT_RESULT = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")


class LinksPageLocators:  # Locator constants for the Links page
    SIMPLE_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")  # 200 Home
    DYNAMIC_LINK = (By.CSS_SELECTOR, "a[id='dynamicLink']")  # 200 HomeDynamic
    LINK_RESPONSE_OUTPUT_RESULT = (By.CSS_SELECTOR, "p[id='linkResponse']")
    CREATED_LINK = (By.CSS_SELECTOR, "a[id='created']")  # 201
    MOVED_LINK = (By.CSS_SELECTOR, "a[id='moved']")  # 301
    BAD_REQUEST_LINK = (By.CSS_SELECTOR, "a[id='bad-request']")  # 400
    UNAUTHORIZED_LINK = (By.CSS_SELECTOR, "a[id='unauthorized']")  # 401
    FORBIDDEN_LINK = (By.CSS_SELECTOR, "a[id='forbidden']")  # 403
    NOTFOUND_LINK = (By.CSS_SELECTOR, "a[id='invalid-url']")  # 404


class UploadDownloadPageLocators:
    """Locator constants for the Upload & Download page."""
    # Upload
    UPLOAD_INPUT = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOADED_RESULT = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')
    # Download
    DOWNLOAD_INPUT = (By.CSS_SELECTOR, 'a[id="downloadButton"]')


class DynamicPropertiesPageLocators:
    """Locator constants for the Dynamic Properties page."""
    ENABLE_AFTER_BUTTON = (By.CSS_SELECTOR, 'button[id="enableAfter"]')
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, 'button[id="colorChange"]')
    VISIBLE_AFTER_BUTTON = (By.CSS_SELECTOR, 'button[id="visibleAfter"]')
