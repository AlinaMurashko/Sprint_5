from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLogout:

    def test_logout_navigate_to_personal_account_and_click_logout_main_page_allows_to_login(self, target_url, registered_credentials, account_link_locator, register_button_class_name, login_input_locator, password_input_locator, logout_button_locator):
        driver = webdriver.Chrome()

        driver.get(target_url)

        driver.find_element(By.XPATH, account_link_locator).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, login_input_locator)))

        driver.find_element(By.XPATH, login_input_locator).send_keys(registered_credentials['email'])
        driver.find_element(By.XPATH, password_input_locator).send_keys(registered_credentials['password'])

        driver.find_element(By.CLASS_NAME, register_button_class_name).click()

        WebDriverWait(driver, 3).until_not(expected_conditions.presence_of_element_located((By.XPATH, login_input_locator)))
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, account_link_locator))).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, logout_button_locator))).click()

        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, login_input_locator)))

        assert driver.find_element(By.XPATH, login_input_locator)

        driver.quit()
