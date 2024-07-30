import time

from conftest import driver
from pages.afw_page import BrowserWindowsPage, AlertsPage, FramesPage


class TestAlertsFrameWindows:

    class TestBrowserWindowsPage:
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

    class TestAlertsPage:
        def test_normal_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()

            alert_text = alerts_page.get_alert_text()
            assert alert_text == 'You clicked a button'

        def test_delay_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()

            alert_text = alerts_page.get_alert_text(delay=6)
            assert alert_text == 'This alert appeared after 5 seconds'

        def test_confirm_box_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()

            text, result_text = alerts_page.get_prompt_alert_text()
            assert result_text == f"You entered {text}"

    class TestFramesPage:
        def test_frames(self, driver):
            frames_page = FramesPage(driver, "https://demoqa.com/frames")
            frames_page.open()

            result_frame1 = frames_page.check_frame_num('frame1')
            result_frame2 = frames_page.check_frame_num('frame2')
            assert result_frame1 == ('This is a sample page', '500px', '350px'), "Error. The first frame doesn't exists."
            assert result_frame2 == ('This is a sample page', '100px', '100px'), "Error. The second frame doesn't exists."
