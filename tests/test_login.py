from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin:

    def test_login_click_on_enter_personal_account_button_login_page_opens(self, target_url, enter_personal_account_button_locator):
        driver = webdriver.Chrome()

        driver.get(target_url)

        driver.find_element(By.XPATH, enter_personal_account_button_locator).click()

        assert driver.current_url == f'{target_url}/login'

        driver.quit()

    def test_login_click_on_personal_account_link_login_page_opens(self, target_url, account_link_locator):
        driver = webdriver.Chrome()

        driver.get(target_url)

        driver.find_element(By.XPATH, account_link_locator).click()

        assert driver.current_url == f'{target_url}/login'

        driver.quit()

    def test_login_navigate_to_registration_page_and_click_on_already_registered_link_login_page_opens(self, target_url, account_link_locator, registration_link_locator, login_link_locator):
        driver = webdriver.Chrome()

        driver.get(target_url)

        driver.find_element(By.XPATH, account_link_locator).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, registration_link_locator)))

        driver.find_element(By.XPATH, registration_link_locator).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, login_link_locator)))

        driver.find_element(By.XPATH, login_link_locator).click()

        assert driver.current_url == f'{target_url}/login'

        driver.quit()

    def test_login_navigate_to_forgot_password_page_and_click_on_remembered_password_link_login_page_opens(self, target_url, account_link_locator, forgot_password_link_locator, login_link_locator):
        driver = webdriver.Chrome()

        driver.get(target_url)

        driver.find_element(By.XPATH, account_link_locator).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, forgot_password_link_locator)))

        driver.find_element(By.XPATH, forgot_password_link_locator).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, login_link_locator)))

        driver.find_element(By.XPATH, login_link_locator).click()

        assert driver.current_url == f'{target_url}/login'

        driver.quit()