from pages.macrodroid_page import MacroDroidPage
from appium.webdriver.common.appiumby import AppiumBy
import time


class StopwatchesPage(MacroDroidPage):
    def __init__(self, driver):
        super().__init__(driver)

        self.stopwatch_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.arlosoft.macrodroid:id/clickContainer").instance(5)')
        self.title = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Stopwatches")')
        self.add_new_stopwatch = (AppiumBy.ID, "com.arlosoft.macrodroid:id/fab")
        self.stopwatch_name_input = (AppiumBy.CLASS_NAME, "android.widget.EditText")
        self.ok_button = (AppiumBy.ID, "com.arlosoft.macrodroid:id/okButton")
        self.get_stopwatch = (AppiumBy.ID, "com.arlosoft.macrodroid:id/stopwatch_name")
        self.play_pause_button = (AppiumBy.ID, "com.arlosoft.macrodroid:id/play_pause_button")
        self.clear_button = (AppiumBy.ID, "com.arlosoft.macrodroid:id/clear_button")
        self.clickable_stopwatch = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.LinearLayout").instance(7)')
        self.rename_stopwatch = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Rename")')
        self.delete_stopwatch = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Delete")')

    def click_stopwatch_button(self):
        self._wait_for_element(self.stopwatch_button).click()

    def is_stopwatch_displayed(self):
        return self._wait_for_element(self.title).is_displayed()

    def click_add_new_stopwatch(self):
        self._wait_for_element(self.add_new_stopwatch).click()

    def name_stopwatch(self):
        el = self._wait_for_element(self.stopwatch_name_input)
        el.clear()
        el.send_keys("automation_test")
        self._wait_for_element(self.ok_button).click()

    def get_stopwatch_name(self):
        return self._wait_for_element(self.get_stopwatch).text

    def click_play_pause_button(self):
        self._wait_for_element(self.play_pause_button).click()
        time.sleep(2)

    def click_clear_button(self):
        self._wait_for_element(self.clear_button).click()

    def click_clickable_stopwatch(self):
        self._wait_for_element(self.clickable_stopwatch).click()

    def click_rename_stopwatch(self):
        self._wait_for_element(self.rename_stopwatch).click()
        el = self._wait_for_element(self.stopwatch_name_input)
        el.clear()
        el.send_keys("test_stopwatch")
        self._wait_for_element(self.ok_button).click()

    def click_delete_stopwatch(self):
        self._wait_for_element(self.delete_stopwatch).click()