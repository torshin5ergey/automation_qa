import time

from conftest import driver
from pages.afw_page import BrowserWindowsPage


class TestAlertsFrameWindows:

    class TestBrowserWindows:
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            new_tab_header = browser_windows_page.get_new_opened_tab_header()
            assert new_tab_header == 'This is a sample page', "Error. The new tab has not opened or incorrect tab header."

        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            new_tab_header = browser_windows_page.get_new_opened_tab_header(open_as='window')
            assert new_tab_header == 'This is a sample page', "Error. The new window has not opened or incorrect tab header."
