from selenium.webdriver.support import expected_conditions as EC
import time


def perform_login(driver, wait, locator):
    wait.until(EC.element_to_be_clickable(locator['authorization']['permission_allow_button'])).click()
    wait.until(EC.element_to_be_clickable(locator['authorization']['close'])).click()
    wait.until(EC.element_to_be_clickable(locator['locator_vkladok']['menu'])).click()
    wait.until(EC.element_to_be_clickable(locator['authorization']['login/registration'])).click()
    wait.until(EC.element_to_be_clickable(locator['authorization']['login_text_editor2'])).click()
    wait.until(EC.element_to_be_clickable(locator['authorization']['login_text_editor2'])).send_keys("7474492708")
    driver.execute_script('mobile: performEditorAction', {'action': 'next'})
    wait.until(EC.element_to_be_clickable(locator['authorization']['pass_text_editor'])).click()
    wait.until(EC.element_to_be_clickable(locator['authorization']['pass_text_editor'])).send_keys("12345test")
    driver.execute_script('mobile: performEditorAction', {'action': 'next'})
    wait.until(EC.element_to_be_clickable(locator['authorization']['login_button'])).click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable(locator['authorization']['permission_allow_button'])).click()
    time.sleep(2)
    for _ in range(8):
        wait.until(EC.element_to_be_clickable(locator['authorization']['password_button'])).click()
        time.sleep(1)
    time.sleep(5)
