import pytest
import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time


@pytest.fixture(scope='function')
def driver():
    desired_cap = UiAutomator2Options()
    desired_cap.platform_name = 'Android'
    desired_cap.device_name = '52001064613fb429'
    desired_cap.automation_name = 'uiautomator2'
    desired_cap.app = 'C:/Users/prost/test/test/python/forautotest.apk'

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=desired_cap)
    driver.implicitly_wait(30)
    yield driver
    driver.quit()


@allure.feature('Registration and Permissions')
@allure.story('User Registration and Permission Handling')
def test_registration_and_permissions(driver):

    with allure.step('Allow permissions'):
        popbtn = driver.find_element(AppiumBy.ID, "com.android.packageinstaller:id/permission_allow_button")
        popbtn.click()

    with allure.step('Open registration page'):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Маска"))).click()

    with allure.step('Login'):
        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Меню\nВкладка 4 из 4")
        popbtn.click()

        # регистрация
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Вход/Регистрация")))
        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Вход/Регистрация")
        popbtn.click()

    with allure.step('Enter phone number'):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="+7"]')))
        element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="+7"]')
        element.click()
        element.send_keys('7474492708')
        driver.execute_script('mobile: performEditorAction', {'action': 'next'})

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@index="1"]')))
        element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@index="1"]')
        element.click()
        element.send_keys('12345test')
        driver.execute_script('mobile: performEditorAction', {'action': 'next'})

    with allure.step('Submit registration'):
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Войти").click()

    with allure.step('Handle additional permissions'):
        driver.find_element(AppiumBy.ID, "com.android.packageinstaller:id/permission_allow_button").click()


@allure.feature('Main Page and My Bank')
@allure.story('Interaction with Main Page and My Bank Section')
def test_main_page_and_my_bank(driver):
    test_registration_and_permissions(driver)
    with allure.step('Navigate to main page'):
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Главная\nВкладка 1 из 4").click()

    with allure.step('Scroll and interact with main page elements'):
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(326, 1155)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(337, 125)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    with allure.step('Navigate to My Bank section'):
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Мой Банк\nВкладка 2 из 4").click()

    with allure.step('Interact with elements in My Bank section'):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Депозит\nот 04.03.2022\n2 000 ₸')))
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Депозит\nот 04.03.2022\n2 000 ₸').click()


@allure.feature('Deposit Selection and State Award Assignment')
@allure.story('Deposit and State Award Interaction')
def test_deposit_and_state_award(driver):
    with allure.step('Select a deposit'):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Депозит\nот 04.03.2022\n2 000 ₸')))
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Депозит\nот 04.03.2022\n2 000 ₸').click()

    with allure.step('Scroll and interact with deposit elements'):
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(316, 960)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(314, 499)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    with allure.step('Navigate to State Award Assignment section'):
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Присвоение Гос. Премии").click()

    with allure.step('Select and confirm state award'):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Депозит\n  от \n15-2022-0003668-1523\nГос. премия\nВыгодный\nНакоплено\n2 000 ₸\nПрогнозируемая премия\n400 ₸")))
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Депозит\n  от \n15-2022-0003668-1523\nГос. премия\nВыгодный\nНакоплено\n2 000 ₸\nПрогнозируемая премия\n400 ₸").click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Выбрать").click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.CheckBox'))).click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Заявление О Начислении Премии Государства').click()
        driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.ImageView[1]').click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Подтвердить').click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@index="2"]')))
        driver.execute_script('mobile: performEditorAction', {'action': 'next'})
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Отправить').click()

    with allure.step('Close application and end test'):
        time.sleep(10)
        driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Закрыть"]').click()
        time.sleep(10)
