from selenium.webdriver.support import expected_conditions as EC
import time

# from glavnaya_vkladka import scroll_to_element


def open_my_bank(wait, driver, all_locators):
    wait.until(EC.element_to_be_clickable(all_locators['locator_vkladok']['my_bank'])).click()
    wait.until(EC.element_to_be_clickable(all_locators['locator_dep']['vybor_depozit'])).click()
    time.sleep(5)
    # scroll_to_element(driver, 'Объединение депозита')
    wait.until(EC.element_to_be_clickable(all_locators['locator_obedinenie_depozita']['obedinenie_depozita'])).click()
    wait.until(EC.element_to_be_clickable(all_locators['locator_butt']['button_next'])).click()
    time.sleep(10)
    wait.until(EC.element_to_be_clickable(all_locators['locator_butt']['button_x'])).click()
    wait.until(EC.element_to_be_clickable(all_locators['locator_butt']['button_close'])).click()
    time.sleep(5)
