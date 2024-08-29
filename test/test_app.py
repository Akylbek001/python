import logging

import pytest
import allure
# import logging
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


@allure.feature('Test')
@allure.story('Sample App Interaction')
def test_app_interaction(driver):
    with allure.step('Аuthorization'):
        popbtn = driver.find_element(AppiumBy.ID, "com.android.packageinstaller:id/permission_allow_button")
        popbtn.click()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Маска")))
        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Маска")
        popbtn.click()

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Меню\nВкладка 4 из 4")
        popbtn.click()

        # регистрация
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Вход/Регистрация")))
        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Вход/Регистрация")
        popbtn.click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="+7"]')))
        element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="+7"]')
        element.click()
        element.send_keys('7013459010')#7474492708
        driver.execute_script('mobile: performEditorAction', {'action': 'next'})

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@index="1"]')))
        element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@index="1"]')
        element.click()
        element.send_keys('12345test')#12345test
        driver.execute_script('mobile: performEditorAction', {'action': 'next'})

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Войти")
        popbtn.click()
        time.sleep(10)

        popbtn = driver.find_element(AppiumBy.ID, "com.android.packageinstaller:id/permission_allow_button")
        popbtn.click()

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Закрыть")
        popbtn.click()

    with allure.step('Main Page and scroll'):
        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Главная\nВкладка 1 из 4")
        popbtn.click()

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(326, 1155)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(337, 125)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(342, 1161)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(342, 104)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    with allure.step('Navigate to My Bank'):
        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Мой Банк\nВкладка 2 из 4")
        popbtn.click()
        time.sleep(10)

    with allure.step('Izmenit uslovia depozita'):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Депозит\nот 22.02.2019\n27 596,55 ₸')))#Депозит\nот 04.03.2022\n2 000 ₸
        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Депозит\nот 22.02.2019\n27 596,55 ₸')
        popbtn.click()
        time.sleep(15)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Маска")))
        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Маска")
        popbtn.click()

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(316, 960)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(314, 399)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        #selevt

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Изменить условия депозита')
        popbtn.click()
        time.sleep(5)

        # Найти элемент с заданным XPath
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@text="1 846 000"]')))
        # Кликнуть на элемент 7 раз
        # for _ in range(7):
        element.click()
        # # Выполнить действие 'previous' на элементе
        # driver.execute_script('mobile: performEditorAction', {'action': 'previous'})
        # Отправить текст в элемент
        element.send_keys('0')

        # Выполнить действие 'next'
        driver.execute_script('mobile: performEditorAction', {'action': 'next'})
        time.sleep(5)
        # for _ in range(6):
        #     driver.execute_script('mobile: performEditorAction', {'action': 'previous '})
        #     time.sleep(1)
        # element = driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.EditText[1]')
        # element.click()
        # element.send_keys('1846000')
        # driver.execute_script('mobile: performEditorAction', {'action': 'next'})

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(368, 1256)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(355, 182)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Изменить условия')
        popbtn.click()

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Подписать')
        popbtn.click()

        driver.execute_script('mobile: performEditorAction', {'action': 'next'})

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(339, 735)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(342, 231)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Отправить")
        popbtn.click()
        time.sleep(10)

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Заявление на изменение условий вклада ЖСС")
        popbtn.click()
        time.sleep(7)

        popbtn = driver.find_element(AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.ImageView[1]")
        popbtn.click()

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Сертификат о наличии вклада ЖСС")
        popbtn.click()
        time.sleep(7)

        popbtn = driver.find_element(AppiumBy.XPATH,
                                     "//android.widget.ScrollView/android.widget.ImageView[1]")
        popbtn.click()

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Депозиты')
        popbtn.click()

    with allure.step('New Dep'):
        # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Навигация назад")
        # popbtn.click()
        # time.sleep(10)

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
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
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.CheckBox')))
        popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox')
        popbtn.click()

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Продолжить")
        popbtn.click()
        time.sleep(15)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText['
                                                                                          '@index="2"]')))
        element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@index="2"]')
        element.click()
        element.send_keys('10200000')
        driver.execute_script('mobile: performEditorAction', {'action': 'next'})

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText'
                                                                                          '[@text="3"]')))
        element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="3"]')
        element.click()
        driver.execute_script('mobile: performEditorAction', {'action': 'next'})

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(359, 755)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(357, 506)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Подтвердить")
        popbtn.click()

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Ознакомиться с условиями")
        popbtn.click()
        time.sleep(10)

        popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.ImageView[1]')
        popbtn.click()

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Подписать")
        popbtn.click()
        time.sleep(10)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText')))

        # element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText')
        # element.send_keys('7\n7\n7\n7\n7\n7')
        driver.execute_script('mobile: performEditorAction', {'action': 'next'})

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Отправить")
        popbtn.click()
        time.sleep(10)

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Депозиты")
        popbtn.click()
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(329, 755)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(329, 618)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    with allure.step('Select a deposit and Select obedinenie dep'):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Депозит\nот 22.02.2019\n27 596,55 ₸')))
        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Депозит\nот 22.02.2019\n27 596,55 ₸')
        popbtn.click()
        time.sleep(15)

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(316, 960)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(314, 499)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Объединение депозита"))
            # Замените на правильный ACCESSIBILITY_ID
        )
        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Объединение депозита")
        popbtn.click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Продолжить"))
            # Замените на правильный ACCESSIBILITY_ID
        )
        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Продолжить")
        popbtn.click()
        time.sleep(20)

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(288, 886)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(290, 564)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        ###1 деп
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Депозит\n  от 22.02.2019\n06-2022-0005251-06\nНакоплено\n27 596,55 ₸\nДоговорная сумма: 27 596,55 ₸"))
            # Замените на правильный ACCESSIBILITY_ID
        )
        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Депозит\n  от 22.02.2019\n06-2022-0005251-06\nНакоплено\n27 596,55 ₸\nДоговорная сумма: 27 596,55 ₸')
        popbtn.click()
        time.sleep(5)

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(339, 841)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(320, 499)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        ###2 деп
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID,
                                              "Депозит\n  от 03.08.2021\n15-2021-14291-1523\nНакоплено\n5 074,72 ₸\nДоговорная сумма: 5 074,72 ₸"))
            # Замените на правильный ACCESSIBILITY_ID
        )
        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Депозит\n  от 03.08.2021\n15-2021-14291-1523\nНакоплено\n5 074,72 ₸\nДоговорная сумма: 5 074,72 ₸')
        popbtn.click()
        time.sleep(5)

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Продолжить')
        popbtn.click()
        time.sleep(10)

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(344, 1064)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(344, 357)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Продолжить')
        popbtn.click()
        time.sleep(10)

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Продолжить')
        popbtn.click()
        time.sleep(10)

        # element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@index="2"]')
        # # element.click()
        # # element.send_keys('777777')
        # driver.execute_script('mobile: performEditorAction', {'action': 'next'})

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(309, 742)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(322, 259)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Отправить')
        popbtn.click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID,
                                              "Депозит\n  от \n15-2021-14291-1523\nВыгодный\nНакоплено\n5 074,72 ₸\nПрогнозируемая премия\n914,122 ₸"))
            # Замените на правильный ACCESSIBILITY_ID
        )
        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID,
                                     "Депозит\n  от \n15-2021-14291-1523\nВыгодный\nНакоплено\n5 074,72 ₸\nПрогнозируемая премия\n914,122 ₸")
        popbtn.click()

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Выбрать')
        popbtn.click()

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Депозиты')
        popbtn.click()

    with allure.step('Zaim_izmenenie_data_platezha'):
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(342, 1152)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(329, 147)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(25)

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Займ от 19.04.2022\nL04725-0202-2022\nВыплачено\n36.0%")
        popbtn.click()
        time.sleep(20)

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(355, 1146)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(348, 532)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(10)

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Изменение даты платежа")
        popbtn.click()
        time.sleep(10)

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Списать")
        popbtn.click()
        time.sleep(8)

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "20")
        popbtn.click()
        time.sleep(5)

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Продолжить")
        popbtn.click()
        time.sleep(5)

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Подтвердить")
        popbtn.click()
        time.sleep(25)

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Подписать")
        popbtn.click()
        time.sleep(10)

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(350, 610)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(344, 268)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Отправить")
        popbtn.click()
        time.sleep(20)

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Подписать")
        popbtn.click()
        time.sleep(10)

        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(359, 612)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(355, 218)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Отправить")
        popbtn.click()
        time.sleep(20)

        popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "На главную")
        popbtn.click()
        time.sleep(10)

    # with allure.step('Polnoe_dosrochnoe_pogoshenie'):
    #     actions = ActionChains(driver)
    #     actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    #     actions.w3c_actions.pointer_action.move_to_location(342, 1152)
    #     actions.w3c_actions.pointer_action.pointer_down()
    #     actions.w3c_actions.pointer_action.move_to_location(329, 147)
    #     actions.w3c_actions.pointer_action.release()
    #     actions.perform()
    #
    #     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID,
    #                                  "Займ от 14.06.2024\nL01003-1600-2024\nВыплачено\n0.0%")
    #     popbtn.click()
    #     time.sleep(20)
    #
    #     actions = ActionChains(driver)
    #     actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    #     actions.w3c_actions.pointer_action.move_to_location(355, 1146)
    #     actions.w3c_actions.pointer_action.pointer_down()
    #     actions.w3c_actions.pointer_action.move_to_location(348, 532)
    #     actions.w3c_actions.pointer_action.release()
    #     actions.perform()
    #
    #     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Полное досрочное погашение")
    #     popbtn.click()
    #     time.sleep(10)
    #
    #     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Откуда")
    #     popbtn.click()
    #     time.sleep(10)
    #
    #     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Текущий счет\n3 010 143,64 ₸")
    #     popbtn.click()
    #     time.sleep(10)
    #
    #     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Продолжить")
    #     popbtn.click()
    #     time.sleep(10)
    #
    #     actions = ActionChains(driver)
    #     actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    #     actions.w3c_actions.pointer_action.move_to_location(352, 1083)
    #     actions.w3c_actions.pointer_action.pointer_down()
    #     actions.w3c_actions.pointer_action.move_to_location(344, 363)
    #     actions.w3c_actions.pointer_action.release()
    #     actions.perform()
    #
    #     WebDriverWait(driver, 10).until(
    #         EC.visibility_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="Я ознакомлен (-а) и уверен (-а), что хочу осуществить досрочное погашение *"]/android.widget.CheckBox')))
    #     popbtn = driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Я ознакомлен (-а) и уверен (-а), что хочу осуществить досрочное погашение *"]/android.widget.CheckBox')
    #     popbtn.click()
    #
    #     WebDriverWait(driver, 10).until(
    #         EC.visibility_of_element_located((AppiumBy.XPATH,
    #                                           '//android.view.View[@content-desc="Я ознакомлен (-а) о невозможности отмены оперции «Полного досрочного погашения» *"]/android.widget.CheckBox')))
    #     popbtn = driver.find_element(AppiumBy.XPATH,
    #                                  '//android.view.View[@content-desc="Я ознакомлен (-а) о невозможности отмены оперции «Полного досрочного погашения» *"]/android.widget.CheckBox')
    #     popbtn.click()
    #     time.sleep(5)
    #
    #     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Продолжить")
    #     popbtn.click()
    #     time.sleep(10)
    #
    #     actions = ActionChains(driver)
    #     actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    #     actions.w3c_actions.pointer_action.move_to_location(333, 1088)
    #     actions.w3c_actions.pointer_action.pointer_down()
    #     actions.w3c_actions.pointer_action.move_to_location(329, 530)
    #     actions.w3c_actions.pointer_action.release()
    #     actions.perform()
    #
    #     WebDriverWait(driver, 10).until(
    #         EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.CheckBox')))
    #     popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox')
    #     popbtn.click()
    #
    #     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Подписать")
    #     popbtn.click()
    #     time.sleep(10)
    #
    #     actions = ActionChains(driver)
    #     actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    #     actions.w3c_actions.pointer_action.move_to_location(363, 612)
    #     actions.w3c_actions.pointer_action.pointer_down()
    #     actions.w3c_actions.pointer_action.move_to_location(361, 376)
    #     actions.w3c_actions.pointer_action.release()
    #     actions.perform()
    #
    #     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Отправить")
    #     popbtn.click()
    #     time.sleep(10)
    #
    #     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "В Мой банк")
    #     popbtn.click()
    #     time.sleep(10)


#     with allure.step('Select prisvoenie gos prem'):
#         WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Депозит\nот 06.04.2017\n255,26 ₸')))
#         popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Депозит\nот 06.04.2017\n255,26 ₸')
#         popbtn.click()
#         time.sleep(15)
#
#         actions = ActionChains(driver)
#         actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
#         actions.w3c_actions.pointer_action.move_to_location(316, 960)
#         actions.w3c_actions.pointer_action.pointer_down()
#         actions.w3c_actions.pointer_action.move_to_location(314, 499)
#         actions.w3c_actions.pointer_action.release()
#         actions.perform()
#
#         popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Присвоение Гос. Премии")
#         popbtn.click()
#
#         actions = ActionChains(driver)
#         actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
#         actions.w3c_actions.pointer_action.move_to_location(331, 538)
#         actions.w3c_actions.pointer_action.pointer_down()
#         actions.w3c_actions.pointer_action.move_to_location(331, 320)
#         actions.w3c_actions.pointer_action.release()
#         actions.perform()
#
#         WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID,
#                                               "Депозит\n  от \n15-2017-04621-1523\nГос. премия\nВыгодный\nНакоплено\n255,26 ₸\nПрогнозируемая премия\n18,608 ₸"))#Депозит\n  от \n15-2022-0003668-1523\nГос. премия\nВыгодный\nНакоплено\n2 000 ₸\nПрогнозируемая премия\n400 ₸
#             #
#         )
#         popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID,
#                                      "Депозит\n  от \n15-2017-04621-1523\nГос. премия\nВыгодный\nНакоплено\n255,26 ₸\nПрогнозируемая премия\n18,608 ₸")
#         popbtn.click()
#
#         popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Выбрать")
#         popbtn.click()
#
#         WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.CheckBox')))
#         popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox')
#         popbtn.click()
#
#         WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Заявление О Начислении Премии Государства')))
#         popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Заявление О Начислении Премии Государства')
#         popbtn.click()
#         time.sleep(8)
#
#         popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.ImageView[1]')
#         popbtn.click()
#
#         WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Условия комплексного банковского обслуживания')))
#         popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Условия комплексного банковского обслуживания')
#         popbtn.click()
#         time.sleep(8)
#
#         popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Закрыть')
#         popbtn.click()
#
#         popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Подтвердить')
#         popbtn.click()
#
#         driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@index="2"]')
#         driver.execute_script('mobile: performEditorAction', {'action': 'next'})
#
#         popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Отправить')
#         popbtn.click()
#         time.sleep(10)
# ###
#         # try:
#         #     expected_accessibility_id = 'Подтверждение\nНа номер +77778262608 отправлено СМС с кодом подтверждения Согласия\nНа выбранном депозите уже присутствует государственная премия'
#         #
#         #     element = WebDriverWait(driver, 10).until(
#         #         EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, expected_accessibility_id))
#         #     )
#         #
#         #     actual_accessibility_id = element.get_attribute('accessibility id')
#         #     assert actual_accessibility_id == expected_accessibility_id
#         # except AssertionError:
#         #     pytest.fail(
#         #         f'Expected accessibility id: "{expected_accessibility_id}", but got: "{actual_accessibility_id}"'
#         # except Exception as e:
#         #     pytest.fail(f'Failed to find element with accessibility id "{expected_accessibility_id}": {str(e)}')
#
#         try:
#             expected_accessibility_id = 'Подтверждение\nНа номер +77026368434 отправлено СМС с кодом подтверждения Согласия\nНа выбранном депозите уже присутствует государственная премия'
#
#             element = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, expected_accessibility_id))
#             )
#
#             actual_accessibility_id = 'Премия государства успешно присвоена'
#             assert actual_accessibility_id == expected_accessibility_id
#         except AssertionError:
#             logging.error(
#                 f'Expected accessibility id: "{expected_accessibility_id}", but got: "{actual_accessibility_id}"')
#             # Обработка ошибки, выполнение кода продолжится
#             try:
#                 popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Депозиты")
#                 popbtn.click()
#                 time.sleep(5)
#             except Exception as e:
#                 logging.error(f'Failed to click "Депозиты": {str(e)}')
#
#         except Exception as e:
#             logging.error(f'Failed to find element with accessibility id "{expected_accessibility_id}": {str(e)}')
#             # Обработка ошибки, выполнение кода продолжится
#             try:
#                 popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Закрыть"]')
#                 popbtn.click()
#                 time.sleep(5)
#             except Exception as e:
#                 logging.error(f'Failed to click "Закрыть": {str(e)}')
#         time.sleep(5)
# ##
#
#     # popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Закрыть"]')
#     # popbtn.click()
#     # time.sleep(5)
#     with allure.step('Navigate to My Bank'):
#         popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Мой Банк\nВкладка 2 из 4")
#         popbtn.click()
#         time.sleep(10)

