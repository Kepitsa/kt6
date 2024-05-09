import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = {
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "appPackage": "com.google.android.calculator",
    "appActivity": "com.android.calculator2.Calculator",
    "automationName": "UiAutomator2",
    "noReset": True
}

appium_server_url = 'http://localhost:4724'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def click_element(self, xpath):
        el = self.driver.find_element(by=AppiumBy.XPATH, value=xpath)
        el.click()

    def delete_all(self):
        clear_button_xpath = '//android.widget.Button[@resource-id="com.google.android.calculator:id/clr"]'
        self.click_element(clear_button_xpath)

    def test_plus(self) -> None:
        self.click_element('//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_7"]')
        self.click_element('//android.widget.Button[@content-desc="plus"]')
        self.click_element('//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_5"]')
        self.click_element('//android.widget.Button[@resource-id="com.google.android.calculator:id/eq"]')
        self.delete_all()

    def test_minus(self) -> None:
        self.click_element('//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_9"]')
        self.click_element('//android.widget.Button[@content-desc="minus"]')
        self.click_element('//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_2"]')
        self.click_element('//android.widget.Button[@resource-id="com.google.android.calculator:id/eq"]')
        self.delete_all()

    def test_multiplication(self) -> None:
        self.click_element('//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_4"]')
        self.click_element('//android.widget.Button[@content-desc="×"]')
        self.click_element('//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_8"]')
        self.click_element('//android.widget.Button[@resource-id="com.google.android.calculator:id/eq"]')
        self.delete_all()

    def test_divide(self) -> None:
        self.click_element('//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_1"]')
        self.click_element('//android.widget.Button[@content-desc="divide"]')
        self.click_element('//android.widget.Button[@resource-id="com.google.android.calculator:id/digit_2"]')
        self.click_element('//android.widget.Button[@resource-id="com.google.android.calculator:id/eq"]')
        self.delete_all()

if __name__ == '__main__':
    unittest.main()
