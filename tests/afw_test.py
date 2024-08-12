import time

import allure

from conftest import driver
from pages.afw_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, ModalDialogsPage


@allure.suite("Alerts, Frame & Windows section")
class TestAlertsFrameWindows:
    @allure.feature("BrowserWindows")
    class TestBrowserWindows:
        @allure.title("Test new tab")
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            new_tab_header = browser_windows_page.get_new_opened_tab_header()
            assert new_tab_header == 'This is a sample page', "Error. The new tab has not opened or incorrect tab header."

        @allure.title("Test new window")
        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            new_tab_header = browser_windows_page.get_new_opened_tab_header(open_as='window')
            assert new_tab_header == 'This is a sample page', "Error. The new window has not opened or incorrect tab header."

    @allure.feature("Alerts")
    class TestAlerts:
        @allure.title("Test normal alert")
        def test_normal_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()

            alert_text = alerts_page.get_alert_text()
            assert alert_text == 'You clicked a button'

        @allure.title("Test delay alert")
        def test_delay_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()

            alert_text = alerts_page.get_alert_text(delay=6)
            assert alert_text == 'This alert appeared after 5 seconds'

        @allure.title("Test confirm box alert")
        def test_confirm_box_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()

            text, result_text = alerts_page.get_prompt_alert_text()
            assert result_text == f"You entered {text}"

    @allure.feature("Frames")
    class TestFrames:
        @allure.title("Test frames")
        def test_frames(self, driver):
            frames_page = FramesPage(driver, "https://demoqa.com/frames")
            frames_page.open()

            result_frame1 = frames_page.get_frame_data('frame1')
            result_frame2 = frames_page.get_frame_data('frame2')
            assert result_frame1 == ('This is a sample page', '500px', '350px'), "Error. The first frame doesn't exists."
            assert result_frame2 == ('This is a sample page', '100px', '100px'), "Error. The second frame doesn't exists."

    @allure.feature("Nested Frames")
    class TestNestedFrames:
        @allure.title("Test nested frames")
        def test_nested_frames(self, driver):
            nested_frames_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            nested_frames_page.open()

            parent_text, child_text = nested_frames_page.get_frames_text()
            assert parent_text == 'Parent frame', "Error. The parent frame doesn't exists."
            assert child_text == 'Child Iframe', "Error. The nested child frame doesn't exists."

    @allure.feature("Modal Dialogs")
    class TestModalDialogs:
        @allure.title("Test small modal window")
        def test_small_modal(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_dialogs_page.open()

            title, text = modal_dialogs_page.get_modal_data('small')
            assert title == 'Small Modal', "Error. Small Modal header is not 'Small Modal'."
            assert len(text) == 47, "Error. Small Modal text is incorrect."

        @allure.title("Test large modal window")
        def test_large_modal(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_dialogs_page.open()

            title, text = modal_dialogs_page.get_modal_data('large')
            assert title == 'Large Modal', "Error. Large Modal header is not 'Large Modal'."
            assert len(text) == 574, "Error. Large Modal text is incorrect."
