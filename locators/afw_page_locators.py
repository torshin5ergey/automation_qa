from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')

    NEW_PAGE_HEADER = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')


class AlertsPageLocators:
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    APPEAR_IN_5SEC_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    CONFIRM_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    PROMPT_ALERT_BUTTON = (By.CSS_SELECTOR, 'button[id="promtButton"]')

    CONFIRM_RESULT_TEXT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    PROMPT_RESULT_TEXT = (By.CSS_SELECTOR, 'span[id="promptResult"]')
