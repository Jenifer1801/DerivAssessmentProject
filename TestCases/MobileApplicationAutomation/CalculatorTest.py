import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By


class Calculator(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            "appium:deviceName": "sdk_gphone64_x86_64",
            "appium:app": "C:\\Users\\jenilobo\\Downloads\\Calculator.apk",
            "appium:platformName": "Android",
            "appium:platformVersion": "12",
            "appium:automationName": "UiAutomator2"
        }
        # Initialize the driver
        options = UiAutomator2Options().load_capabilities(desired_caps)
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

    def test_add(self):
        self.driver.find_element(By.ID, 'com.google.android.calculator:id/digit_8').click()
        self.driver.find_element(By.ID, 'com.google.android.calculator:id/op_add').click()
        self.driver.find_element(By.ID, 'com.google.android.calculator:id/digit_4').click()
        self.driver.find_element(By.ID, 'com.google.android.calculator:id/eq').click()
        addResult = self.driver.find_element(By.ID, 'com.google.android.calculator:id/result_final').text
        print(addResult)
        assert (addResult == "12")

    def test_sub(self):
        driver = self.driver
        driver.find_element(By.ID, 'com.google.android.calculator:id/digit_8').click()
        driver.find_element(By.ID, 'com.google.android.calculator:id/op_sub').click()
        driver.find_element(By.ID, 'com.google.android.calculator:id/digit_4').click()
        driver.find_element(By.ID, 'com.google.android.calculator:id/eq').click()
        subResult = driver.find_element(By.ID, 'com.google.android.calculator:id/result_final').text
        print(subResult)
        assert (subResult == "4")

    def test_mul(self):
        driver = self.driver
        driver.find_element(By.ID, 'com.google.android.calculator:id/digit_8').click()
        driver.find_element(By.ID, 'com.google.android.calculator:id/op_mul').click()
        driver.find_element(By.ID, 'com.google.android.calculator:id/digit_4').click()
        driver.find_element(By.ID, 'com.google.android.calculator:id/eq').click()
        mulResult = driver.find_element(By.ID, 'com.google.android.calculator:id/result_final').text
        print(mulResult)

    def test_div(self):
        driver = self.driver
        driver.find_element(By.ID, 'com.google.android.calculator:id/digit_8').click()
        driver.find_element(By.ID, 'com.google.android.calculator:id/op_div').click()
        driver.find_element(By.ID, 'com.google.android.calculator:id/digit_4').click()
        driver.find_element(By.ID, 'com.google.android.calculator:id/eq').click()
        divResult = driver.find_element(By.ID, 'com.google.android.calculator:id/result_final').text
        print(divResult)
        assert (divResult == "2")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
