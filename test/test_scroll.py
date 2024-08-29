from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput
# import time

# Настройка
desired_cap = UiAutomator2Options()
desired_cap.platform_name = 'Android'
desired_cap.device_name = '52001064613fb429'
desired_cap.automation_name = 'UiAutomator2'
desired_cap.app = 'C:/Users/prost/test/test/python/forautotest.apk'

# Создание драйвера
driver = webdriver.Remote("http://127.0.0.1:4723", options=desired_cap)

# Установка неявного ожидания
driver.implicitly_wait(30)

# Поиск и нажатие на кнопку разрешения
try:
     popbtn = driver.find_element(AppiumBy.ID, "com.android.packageinstaller:id/permission_allow_button")
     popbtn.click()
#
#     # Явное ожидание на успешное выполнение предыдущего действия
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Маска")))
#
#     # Поиск и нажатие на элемент с content-desc
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Маска")
#     popbtn.click()
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Меню\nВкладка 4 из 4")
#     popbtn.click()
# ### РЕГИСТРАЦИЯ НАЧАЛА
#     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Вход/Регистрация")))
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Вход/Регистрация")
#     popbtn.click()
#
#     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText'
#                                                                                       '[@text="+7"]')))
#
#     element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="+7"]')
#     element.click()
#     element.send_keys('7001867334')#7474492708
#     driver.execute_script('mobile: performEditorAction', {'action': 'next'})
#
#     WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@index="1"]')))
#
#     element = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@index="1"]')
#     element.click()
#     element.send_keys('12345test')#Aa123456@
#     driver.execute_script('mobile: performEditorAction', {'action': 'next'})
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Войти")
#     popbtn.click()
#
#     popbtn = driver.find_element(AppiumBy.ID, "com.android.packageinstaller:id/permission_allow_button")
#     popbtn.click()
# ### РЕГИСТРАЦИЯ КОНЕЦ
#
#     WebDriverWait(driver, 20).until(
#         EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "2"))  # Замените на правильный ACCESSIBILITY_ID
#     )
#
#     # Поиск элемента один раз
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "2")
#
#     # Нажимаем на кнопку 8 раз
#     for _ in range(8):
#         # Явное ожидание до тех пор, пока элемент станет кликабельным
#         WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "2"))  # Замените на правильный ACCESSIBILITY_ID
#         )
#         popbtn.click()
#         time.sleep(1)  # Подождем 1 секунду между нажатиями (по необходимости)
#     time.sleep(10)
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Мой Банк\nВкладка 2 из 4")
#     popbtn.click()
#     time.sleep(10)
#
#     actions = ActionChains(driver)
#     actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
#     actions.w3c_actions.pointer_action.move_to_location(342, 1152)
#     actions.w3c_actions.pointer_action.pointer_down()
#     actions.w3c_actions.pointer_action.move_to_location(329, 147)
#     actions.w3c_actions.pointer_action.release()
#     actions.perform()
#
#     popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Займ от 05.02.2021\nF00804-0200-2021\nВыплачено\n38.0%")
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
#ИЗМЕНЕНИЕ ДАТЫ ПЛАТЕЖА НАЧАЛА
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Изменение даты платежа")
    # popbtn.click()
    # time.sleep(10)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Изменение даты платежа")
    # popbtn.click()
    # time.sleep(15)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "20")
    # popbtn.click()
    # time.sleep(10)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Продолжить")
    # popbtn.click()
    # time.sleep(10)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Подтвердить")
    # popbtn.click()
    # time.sleep(10)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Подписать")
    # popbtn.click()
    # time.sleep(10)
    #
    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(350, 610)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(344, 268)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Отправить")
    # popbtn.click()
    # time.sleep(30)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Подписать")
    # popbtn.click()
    # time.sleep(10)
    #
    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(359, 612)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(355, 218)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Отправить")
    # popbtn.click()
    # time.sleep(25)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "На главную")
    # popbtn.click()
    # time.sleep(10)
#ИЗМЕНЕНИЕ ДАТЫ ПЛАТЕЖА КОНЕЦ
#ПЕРЕХОД НА ЖИЛ ЗАЕМ НАЧАЛА
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Переход на жилищный заем")
    # popbtn.click()
    # time.sleep(10)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Продолжить")
    # popbtn.click()
    # time.sleep(10)
#ПЕРЕХОД НА ЖИЛ ЗАЕМ КОНЕЦ
#ПДП НАЧАЛА
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Полное досрочное погашение")
    # popbtn.click()
    # time.sleep(10)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Откуда")
    # popbtn.click()
    # time.sleep(10)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Текущий счет\n3 010 143,64 ₸")
    # popbtn.click()
    # time.sleep(10)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Продолжить")
    # popbtn.click()
    # time.sleep(10)
    #
    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(352, 1083)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(344, 363)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="Я ознакомлен (-а) и уверен (-а), что хочу осуществить досрочное погашение *"]/android.widget.CheckBox')))
    # popbtn = driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Я ознакомлен (-а) и уверен (-а), что хочу осуществить досрочное погашение *"]/android.widget.CheckBox')
    # popbtn.click()
    #
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.XPATH,
    #                                       '//android.view.View[@content-desc="Я ознакомлен (-а) о невозможности отмены оперции «Полного досрочного погашения» *"]/android.widget.CheckBox')))
    # popbtn = driver.find_element(AppiumBy.XPATH,
    #                              '//android.view.View[@content-desc="Я ознакомлен (-а) о невозможности отмены оперции «Полного досрочного погашения» *"]/android.widget.CheckBox')
    # popbtn.click()
    # time.sleep(5)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Продолжить")
    # popbtn.click()
    # time.sleep(10)
    #
    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(333, 1088)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(329, 530)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.CheckBox')))
    # popbtn = driver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox')
    # popbtn.click()
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Подписать")
    # popbtn.click()
    # time.sleep(10)
    #
    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(363, 612)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(361, 376)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Отправить")
    # popbtn.click()
    # time.sleep(10)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "В Мой банк")
    # popbtn.click()
    # time.sleep(10)
#ПДП КОНЕЦ
#ЧДП НАЧАЛА
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Частичное досрочное погашение")
    # popbtn.click()
    # time.sleep(10)
    #
    # popbtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Частичное досрочное погашение")
    # popbtn.click()
    # time.sleep(10)
#ЧДП КОНЕЦ
except Exception as e:
    print(f"An error occurred: {e}")

# Завершение работы с драйвером
finally:
    driver.quit()