import pytest
import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.feature('Registration and Permissions')
@allure.story('User Registration and Permission Handling')
def test_registration_and_permissions(driver):
    with allure.step('Allow permissions'):
        popbtn = driver.find_element(AppiumBy.ID, "com.android.packageinstaller:id/permission_allow_button")
        popbtn.click()

    with allure.step('Open registration page'):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Маска"))).click()

    with allure.step('Enter phone number'):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="+7"]'))).send_keys(
            '7474492708')
        driver.execute_script('mobile: performEditorAction', {'action': 'next'})

    with allure.step('Enter password'):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@index="1"]'))).send_keys(
            '12345test')
        driver.execute_script('mobile: performEditorAction', {'action': 'next'})

    with allure.step('Submit registration'):
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Войти").click()

    with allure.step('Handle additional permissions'):
        driver.find_element(AppiumBy.ID, "com.android.packageinstaller:id/permission_allow_button").click()
