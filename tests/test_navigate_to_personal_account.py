from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestNavigateToPersonalAccount:
    
    def test_login_succesfully_click_on_personal_account_link_personal_account_page_opens(self, target_url, account_link_locator, login_input_locator, password_input_locator, registered_credentials, register_button_class_name, logout_button_locator):
        driver = webdriver.Chrome()

        driver.get(target_url)

        driver.find_element(By.XPATH, account_link_locator).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, login_input_locator)))

        driver.find_element(By.XPATH, login_input_locator).send_keys(registered_credentials['email'])
        driver.find_element(By.XPATH, password_input_locator).send_keys(registered_credentials['password'])

        driver.find_element(By.CLASS_NAME, register_button_class_name).click()

        WebDriverWait(driver, 3).until_not(expected_conditions.presence_of_element_located((By.XPATH, login_input_locator)))

        driver.find_element(By.XPATH, account_link_locator).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, logout_button_locator)))

        assert driver.current_url == f'{target_url}/account/profile'

        driver.quit()