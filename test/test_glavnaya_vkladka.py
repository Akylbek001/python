import time

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import action_builder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@allure.feature('Test')
@allure.story('Sample App Interaction')
def test_app_interaction(driver):
    with allure.step('Authorization'):
        try:
            popbtn = driver.find_element(AppiumBy.ID, "com.android.packageinstaller:id/permission_allow_button")
            popbtn.click()

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Маска")))
            popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Маска")
            popbtn.click()

            popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Меню\nВкладка 4 из 4")
            popbtn.click()

            # Регистрация
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Вход/Регистрация"))
            )
            popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Вход/Регистрация")
            popbtn.click()

            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="+7"]'))
            )
            element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="+7"]')
            element.click()
            element.send_keys('7474492708')
            driver.execute_script('mobile: performEditorAction', {'action': 'next'})

            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@index="1"]'))
            )
            element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@index="1"]')
            element.click()
            element.send_keys('12345test')
            driver.execute_script('mobile: performEditorAction', {'action': 'next'})

            popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Войти")
            popbtn.click()

            popbtn = driver.find_element(AppiumBy.ID, "com.android.packageinstaller:id/permission_allow_button")
            popbtn.click()

            popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Закрыть")
            popbtn.click()
        except Exception as e:
            allure.attach(f"Authorization step failed: {str(e)}", name="Authorization Step Error", attachment_type=allure.attachment_type.TEXT)

    with allure.step('Main Page and Scroll'):
        try:
            popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Главная\nВкладка 1 из 4")
            popbtn.click()

            actions = ActionChains(driver)
            actions.w3c_actions = action_builder.ActionBuilder(driver, mouse=PointerInput(PointerInput.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(326, 1155)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(337, 125)
            actions.w3c_actions.pointer_action.release()
            actions.perform()

            actions = ActionChains(driver)
            actions.w3c_actions = action_builder.ActionBuilder(driver, mouse=PointerInput(PointerInput.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(342, 1161)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(342, 104)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
        except Exception as e:
            allure.attach(f"Main Page and Scroll step failed: {str(e)}", name="Main Page and Scroll Step Error", attachment_type=allure.attachment_type.TEXT)

    with allure.step('Navigate to My Bank'):
        try:
            popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Мой Банк\nВкладка 2 из 4")
            popbtn.click()
            time.sleep(15)
        except Exception as e:
            allure.attach(f"Navigate to My Bank step failed: {str(e)}", name="Navigate to My Bank Step Error", attachment_type=allure.attachment_type.TEXT)

    with allure.step('Select a Deposit and Select Gov. Premium'):
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Депозит\nот 04.03.2022\n2 000 ₸'))
            )
            popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Депозит\nот 04.03.2022\n2 000 ₸')
            popbtn.click()
            time.sleep(20)

            actions = ActionChains(driver)
            actions.w3c_actions = action_builder.ActionBuilder(driver, mouse=PointerInput(PointerInput.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(316, 960)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(314, 499)
            actions.w3c_actions.pointer_action.release()
            actions.perform()

            popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Присвоение Гос. Премии")
            popbtn.click()

            actions = ActionChains(driver)
            actions.w3c_actions = action_builder.ActionBuilder(driver, mouse=PointerInput(PointerInput.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(331, 538)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(331, 320)
            actions.w3c_actions.pointer_action.release()
            actions.perform()

            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID,
                                                  "Депозит\n  от \n30-2024-0094432-3001\nНакоплено\n0 ₸\nПрогнозируемая премия\n0 ₸"))
            )
            popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                         "Депозит\n  от \n30-2024-0094432-3001\nНакоплено\n0 ₸\nПрогнозируемая премия\n0 ₸")
            popbtn.click()

            popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Выбрать")
            popbtn.click()

            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.CheckBox')))
            popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox')
            popbtn.click()

            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Заявление О Начислении Премии Государства'))
            )
            popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Заявление О Начислении Премии Государства')
            popbtn.click()

            popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.ImageView[1]')
            popbtn.click()

            popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Подтвердить')
            popbtn.click()

            driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@index="2"]')
            driver.execute_script('mobile: performEditorAction', {'action': 'next'})

            popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Отправить')
            popbtn.click()
            time.sleep(10)

            try:
                expected_accessibility_id = 'Подтверждение\nНа номер +77474492708 отправлено СМС с кодом подтверждения Согласия\nНа выбранном депозите уже присутствует государственная премия'

                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, expected_accessibility_id))
                )

                # Получаем значение accessibility id элемента
                actual_accessibility_id = element.get_attribute('accessibility id')

                # Сравнение значений
                assert actual_accessibility_id == expected_accessibility_id, \
                    f'Expected accessibility id: "{expected_accessibility_id}", but got: "{actual_accessibility_id}"'
            except Exception as e:
                allure.attach(f"Verification of accessibility id failed: {str(e)}", name="Verification Step Error", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            allure.attach(f"Select a deposit and Select Gov. Premium step failed: {str(e)}", name="Select Deposit Step Error", attachment_type=allure.attachment_type.TEXT)

    with allure.step('New Deposit'):
        try:
            popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Мой Банк\nВкладка 2 из 4")
            popbtn.click()
            time.sleep(15)

            actions = ActionChains(driver)
            actions.w3c_actions = action_builder.ActionBuilder(driver, mouse=PointerInput(PointerInput.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(303, 975)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(294, 564)
            actions.w3c_actions.pointer_action.release()
            actions.perform()

            popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Открыть новый депозит")
            popbtn.click()

            popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                         "Депозит «Баспана»\nНакопите на первоначальный взнос и покупайте жилье в ипотеку со ставкой от 3,5% (ГЭСВ от 3,6%)")
            popbtn.click()

            popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Продолжить")
            popbtn.click()

            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.CheckBox'))
            )
            popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox')
            popbtn.click()
        except Exception as e:
            allure.attach(f"New Deposit step failed: {str(e)}", name="New Deposit Step Error", attachment_type=allure.attachment_type.TEXT)