from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestRegistration:
    def test_registration_provide_valid_credentials_registration_is_successful(self, target_url, email, password, account_link_locator, registration_link_locator):
        driver = webdriver.Chrome()

        driver.get(target_url)

        driver.find_element(By.XPATH, account_link_locator).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, registration_link_locator)))

        driver.find_element(By.XPATH, registration_link_locator).click()

        assert driver.current_url == f'{target_url}/register'

        for element in driver.find_elements(By.XPATH, './/input[@name="name"]'):
            element.send_keys(email)

        driver.find_element(By.XPATH, './/input[@type="password"]').send_keys(password)

        driver.find_element(By.CLASS_NAME, 'button_button_type_primary__1O7Bx').click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, registration_link_locator)))

        assert driver.current_url == f'{target_url}/login'

        driver.quit()

    def test_registration_provide_unacceptable_password_registration_is_forbidden(self, target_url, email, account_link_locator, registration_link_locator):
        driver = webdriver.Chrome()

        driver.get(target_url)

        driver.find_element(By.XPATH, account_link_locator).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, registration_link_locator)))

        driver.find_element(By.XPATH, registration_link_locator).click()

        assert driver.current_url == f'{target_url}/register'

        for element in driver.find_elements(By.XPATH, './/input[@name="name"]'):
            element.send_keys(email)

        driver.find_element(By.XPATH, './/input[@type="password"]').send_keys("short")

        driver.find_element(By.CLASS_NAME, 'button_button_type_primary__1O7Bx').click()

        assert driver.current_url != f'{target_url}/login'

        driver.quit()