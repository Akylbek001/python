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

# Настройка
desired_cap = UiAutomator2Options()
desired_cap.platform_name = 'Android'
desired_cap.device_name = '52001064613fb429'
desired_cap.automation_name = 'uiautomator2'
desired_cap.app = 'C:/Users/prost/test/test/python/forautotest.apk'

# Создание драйвера
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=desired_cap)

# Установка неявного ожидания
driver.implicitly_wait(30)

# Поиск и нажатие на кнопку разрешения
try:
    popbtn = driver.find_element(AppiumBy.ID, "com.android.packageinstaller:id/permission_allow_button")
    popbtn.click()

    # Явное ожидание на успешное выполнение предыдущего действия
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Маска")))

    # Поиск и нажатие на элемент с content-desc
    popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Маска")
    popbtn.click()

    popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Меню\nВкладка 4 из 4")
    popbtn.click()
### РЕГИСТРАЦИЯ НАЧАЛА
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Вход/Регистрация")))
    popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Вход/Регистрация")
    popbtn.click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText'
                                                                                      '[@text="+7"]')))

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

    popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Войти")
    popbtn.click()

    popbtn = driver.find_element(AppiumBy.ID, "com.android.packageinstaller:id/permission_allow_button")
    popbtn.click()
### РЕГИСТРАЦИЯ КОНЕЦ

    popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Закрыть")
    popbtn.click()

    # WebDriverWait(driver, 20).until(
    #     EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "2"))  # Замените на правильный ACCESSIBILITY_ID
    # )
    #
    # # Поиск элемента один раз
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "2")
    #
    # # Нажимаем на кнопку 8 раз
    # for _ in range(8):
    #     # Явное ожидание до тех пор, пока элемент станет кликабельным
    #     WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "2"))  # Замените на правильный ACCESSIBILITY_ID
    #     )
    #     popbtn.click()
    #     time.sleep(1)  # Подождем 1 секунду между нажатиями (по необходимости)
    # time.sleep(10)

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

    popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Мой Банк\nВкладка 2 из 4")
    popbtn.click()
    time.sleep(15)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Депозит\nот 04.03.2022\n2 000 ₸')))
    popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Депозит\nот 04.03.2022\n2 000 ₸')
    popbtn.click()
    time.sleep(20)

    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(309, 1083)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(337, 437)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()

###ОБЪЕДИНЕНИЕ ДЕПОЗИТА ЕСЛИ ЕСТЬ ТОЛЬКО 1 ДЕП.    начала
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Объединение депозита"))
    #     # Замените на правильный ACCESSIBILITY_ID
    # )
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Объединение депозита")
    # popbtn.click()
    #
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Продолжить"))
    #     # Замените на правильный ACCESSIBILITY_ID
    # )
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Продолжить")
    # popbtn.click()
    #
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView[@index="0"]')))
    # popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@index="0"]')
    # popbtn.click()
    #
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Закрыть"))
    #     # Замените на правильный ACCESSIBILITY_ID
    # )
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Закрыть")
    # popbtn.click()
## конец

    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(316, 960)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(314, 499)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

###ПРИСВОЕНИЕ Г.П. С 1 ДЕП
    popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Присвоение Гос. Премии")
    popbtn.click()

    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(331, 538)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(331, 320)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Депозит\n  от \n15-2022-0003668-1523\nГос. премия\nВыгодный\nНакоплено\n2 000 ₸\nПрогнозируемая премия\n400 ₸"))
        # Замените на правильный ACCESSIBILITY_ID
    )
    popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Депозит\n  от \n15-2022-0003668-1523\nГос. премия\nВыгодный\nНакоплено\n2 000 ₸\nПрогнозируемая премия\n400 ₸")
    popbtn.click()

    popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Выбрать")
    popbtn.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.CheckBox')))
    popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox')
    popbtn.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Заявление О Начислении Премии Государства')))
    popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Заявление О Начислении Премии Государства')
    popbtn.click()

    popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.ImageView[1]')
    popbtn.click()

    popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Подтвердить')
    popbtn.click()

    element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@index="2"]')
    # element.click()
    # element.send_keys('7\n7\n7\n7\n7\n7')
    driver.execute_script('mobile: performEditorAction', {'action': 'next'})

    popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Отправить')
    popbtn.click()
    time.sleep(10)

    popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Закрыть"]')
    popbtn.click()
    time.sleep(10)
## КОНЕЦ
##ОТКРЫТЬ НОВЫЙ ДЕПОЗИТ

    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Мой Банк\nВкладка 2 из 4")
    # popbtn.click()
#     actions = ActionChains(driver)
#     actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
#     actions.w3c_actions.pointer_action.move_to_location(303, 975)
#     actions.w3c_actions.pointer_action.pointer_down()
#     actions.w3c_actions.pointer_action.move_to_location(294, 564)
#     actions.w3c_actions.pointer_action.release()
#     actions.perform()
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Открыть новый депозит")
#     popbtn.click()
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Депозит «Баспана»\nНакопите на первоначальный взнос и покупайте жилье в ипотеку со ставкой от 3,5% (ГЭСВ от 3,6%)")
#     popbtn.click()
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Продолжить")
#     popbtn.click()
#
#     WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.CheckBox')))
#     popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox')
#     popbtn.click()
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Продолжить")
#     popbtn.click()
#     time.sleep(15)
#
#     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText['
#                                                                                       '@index="2"]')))
#     element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@index="2"]')
#     element.click()
#     element.send_keys('9520000')
#     driver.execute_script('mobile: performEditorAction', {'action': 'next'})
#
#     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText'
#                                                                                       '[@text="3"]')))
#     element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="3"]')
#     element.click()
#     driver.execute_script('mobile: performEditorAction', {'action': 'next'})
#
#     actions = ActionChains(driver)
#     actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
#     actions.w3c_actions.pointer_action.move_to_location(359, 755)
#     actions.w3c_actions.pointer_action.pointer_down()
#     actions.w3c_actions.pointer_action.move_to_location(357, 506)
#     actions.w3c_actions.pointer_action.release()
#     actions.perform()
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Подтвердить")
#     popbtn.click()
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Ознакомиться с условиями")
#     popbtn.click()
#
#     popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.ImageView[1]')
#     popbtn.click()
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Подписать")
#     popbtn.click()
#     time.sleep(10)
#
#     WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText')))
#
#     # element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText')
#     # element.send_keys('7\n7\n7\n7\n7\n7')
#     driver.execute_script('mobile: performEditorAction', {'action': 'next'})
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Отправить")
#     popbtn.click()
#     time.sleep(10)
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Депозиты")
#     popbtn.click()
#     actions = ActionChains(driver)
#     actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
#     actions.w3c_actions.pointer_action.move_to_location(329, 755)
#     actions.w3c_actions.pointer_action.pointer_down()
#     actions.w3c_actions.pointer_action.move_to_location(329, 618)
#     actions.w3c_actions.pointer_action.release()
#     actions.perform()
# ##конец
# ##ОТКРЫТЬ ЕЩЕ ДЕПОЗИТ
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Мой Банк\nВкладка 2 из 4")
#     popbtn.click()
#
#     actions = ActionChains(driver)
#     actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
#     actions.w3c_actions.pointer_action.move_to_location(303, 975)
#     actions.w3c_actions.pointer_action.pointer_down()
#     actions.w3c_actions.pointer_action.move_to_location(294, 564)
#     actions.w3c_actions.pointer_action.release()
#     actions.perform()
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Открыть новый депозит")
#     popbtn.click()
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID,
#                                  "Депозит «Баспана»\nНакопите на первоначальный взнос и покупайте жилье в ипотеку со ставкой от 3,5% (ГЭСВ от 3,6%)")
#     popbtn.click()
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Продолжить")
#     popbtn.click()
#
#     WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.CheckBox')))
#     popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox')
#     popbtn.click()
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Продолжить")
#     popbtn.click()
#     time.sleep(15)
#
#     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText['
#                                                                                       '@index="2"]')))
#     element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@index="2"]')
#     element.click()
#     element.send_keys('8000000')
#     driver.execute_script('mobile: performEditorAction', {'action': 'next'})
#
#     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText'
#                                                                                       '[@text="3"]')))
#     element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="3"]')
#     element.click()
#     driver.execute_script('mobile: performEditorAction', {'action': 'next'})
#
#     actions = ActionChains(driver)
#     actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
#     actions.w3c_actions.pointer_action.move_to_location(359, 755)
#     actions.w3c_actions.pointer_action.pointer_down()
#     actions.w3c_actions.pointer_action.move_to_location(357, 506)
#     actions.w3c_actions.pointer_action.release()
#     actions.perform()
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Подтвердить")
#     popbtn.click()
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Ознакомиться с условиями")
#     popbtn.click()
#
#     popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.ImageView[1]')
#     popbtn.click()
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Подписать")
#     popbtn.click()
#     time.sleep(10)
#
#     WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText')))
#
#     # element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText')
#     # element.send_keys('7\n7\n7\n7\n7\n7')
#     driver.execute_script('mobile: performEditorAction', {'action': 'next'})
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Отправить")
#     popbtn.click()
#     time.sleep(10)
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Депозиты")
#     popbtn.click()
#     actions = ActionChains(driver)
#     actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
#     actions.w3c_actions.pointer_action.move_to_location(329, 755)
#     actions.w3c_actions.pointer_action.pointer_down()
#     actions.w3c_actions.pointer_action.move_to_location(329, 618)
#     actions.w3c_actions.pointer_action.release()
#     actions.perform()
# КОНЕЦ ДЕПОЗИТА

### Присвоение с пустых депозитов
    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(331, 296)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(335, 729)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()

    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Мой Банк\nВкладка 2 из 4')
    # popbtn.click()
    # time.sleep(10)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Все 7')
    # popbtn.click()
    # time.sleep(10)
    #
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Депозит   от 04.03.2022\nАльтернативный код\n151016142973\nГос. премия\nНакоплено\n2 000 ₸')))
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Депозит   от 04.03.2022\nАльтернативный код\n151016142973\nГос. премия\nНакоплено\n2 000 ₸')
    # popbtn.click()
    # time.sleep(20)
    #
    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(324, 1081)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(322, 532)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Присвоение Гос. Премии")
    # popbtn.click()
    # time.sleep(10)
    #
    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(333, 1008)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(311, 456)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    # # time.sleep(10)
    #
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID,
    #                                       "Депозит\n  от \n30-2024-0090700-3001\nНакоплено\n0 ₸\nПрогнозируемая премия\n0 ₸"))
    #     # Замените на правильный ACCESSIBILITY_ID
    # )
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID,
    #                              "Депозит\n  от \n30-2024-0090700-3001\nНакоплено\n0 ₸\nПрогнозируемая премия\n0 ₸")
    # popbtn.click()
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Выбрать")
    # popbtn.click()
    #
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.CheckBox')))
    # popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox')
    # popbtn.click()
    #
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Заявление О Начислении Премии Государства')))
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Заявление О Начислении Премии Государства')
    # popbtn.click()
    #
    # popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.ImageView[1]')
    # popbtn.click()
    #
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Условия комплексного банковского обслуживания')))
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Условия комплексного банковского обслуживания')
    # popbtn.click()
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Закрыть')
    # popbtn.click()
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Подтвердить')
    # popbtn.click()
    #
    # element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@index="2"]')
    # driver.execute_script('mobile: performEditorAction', {'action': 'next'})
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Отправить')
    # popbtn.click()
    # time.sleep(15)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Депозиты')
    # popbtn.click()
### конец

## Объединение 2 депозита
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Депозит\nот 04.03.2022\n2 000 ₸')))
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Депозит\nот 04.03.2022\n2 000 ₸')
    # popbtn.click()
    # time.sleep(20)
    #
    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(324, 1081)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(322, 532)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    # time.sleep(5)

    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Объединение депозита"))
    #     # Замените на правильный ACCESSIBILITY_ID
    # )
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Объединение депозита")
    # popbtn.click()
    #
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Продолжить"))
    #     # Замените на правильный ACCESSIBILITY_ID
    # )
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Продолжить")
    # popbtn.click()
    # time.sleep(10)
    #
    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(288, 886)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(290, 564)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # ###1 деп
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Депозит\n  от 19.08.2024\n30-2024-0090700-3001\nНакоплено\n0 ₸\nДоговорная сумма: 0 ₸"))
    #     # Замените на правильный ACCESSIBILITY_ID
    # )
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Депозит\n  от 19.08.2024\n30-2024-0090700-3001\nНакоплено\n0 ₸\nДоговорная сумма: 0 ₸')
    # popbtn.click()
    # time.sleep(5)
    #
    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(339, 841)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(320, 499)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # ###2 деп
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID,
    #                                       "Депозит\n  от 19.08.2024\n30-2024-0090701-3001\nНакоплено\n0 ₸\nДоговорная сумма: 0 ₸"))
    #     # Замените на правильный ACCESSIBILITY_ID
    # )
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Депозит\n  от 19.08.2024\n30-2024-0090701-3001\nНакоплено\n0 ₸\nДоговорная сумма: 0 ₸')
    # popbtn.click()
    # time.sleep(5)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Продолжить')
    # popbtn.click()
    # time.sleep(25)
    #
    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(344, 1064)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(344, 357)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Продолжить')
    # popbtn.click()
    # time.sleep(10)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Продолжить')
    # popbtn.click()
    # time.sleep(5)
    #
    # # element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@index="2"]')
    # # # element.click()
    # # # element.send_keys('777777')
    # # driver.execute_script('mobile: performEditorAction', {'action': 'next'})
    #
    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(309, 742)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(322, 259)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Отправить')
    # popbtn.click()
    #
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID,
    #                                       "Депозит\n  от \n15-2022-0003668-1523\nВыгодный\nНакоплено\n2 000 ₸\nПрогнозируемая премия\n400 ₸"))
    #     # Замените на правильный ACCESSIBILITY_ID
    # )
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID,
    #                              "Депозит\n  от \n15-2022-0003668-1523\nВыгодный\nНакоплено\n2 000 ₸\nПрогнозируемая премия\n400 ₸")
    # popbtn.click()
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Выбрать')
    # popbtn.click()
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Депозиты')
    # popbtn.click()
# #конец
###ДЕЛЕНИЕ ДЕПОЗИТА
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Депозит\nот 19.08.2024\n0 ₸")
#     popbtn.click()
#     time.sleep(15)
#
    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(324, 1081)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(322, 532)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Деление депозита")
    # popbtn.click()
    # time.sleep(10)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Разделить")
    # popbtn.click()
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "К заявке")
    # popbtn.click()
    # time.sleep(10)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Навигация назад")
    # popbtn.click()
    # time.sleep(10)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Навигация назад")
    # popbtn.click()
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Навигация назад")
    # popbtn.click()
### КОНЕЦ
#
# ### РАСТОРЖЕНИЕ ДЕПОЗИТА НАЧАЛА
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Депозит\nот 04.03.2022\n2 000 ₸")
#     popbtn.click()
#     time.sleep(15)
#
    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(333, 1070)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(331, 560)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Расторжение депозита")
    # popbtn.click()
    # time.sleep(10)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Расторгнуть")
    # popbtn.click()
    # time.sleep(10)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Продолжить")
    # popbtn.click()
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "К заявке")
    # popbtn.click()
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Навигация назад")
    # popbtn.click()
    # time.sleep(10)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Навигация назад")
    # popbtn.click()
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Навигация назад")
    # popbtn.click()
    # time.sleep(10)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Главная\nВкладка 1 из 4")
    # popbtn.click()

### РАСТОРЖЕНИЕ КОНЕЦ

except Exception as e:
    print(f"An error occurred: {e}")

# finally:
#     driver.quit()
# Завершение работы с драйвером
