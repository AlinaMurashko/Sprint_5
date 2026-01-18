import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import BASE_URL, LOGIN_URL, REGISTER_URL
from locators import HomePageLocators, LoginPageLocators, RegistrationPageLocators
from data import generate_random_email, get_test_password

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 3)

@pytest.fixture
def registered_credentials(driver, wait):
        email = generate_random_email()
        password = get_test_password()

        driver.get(BASE_URL)

        driver.find_element(*HomePageLocators.PERSONAL_ACCOUNT_LINK).click()

        wait.until(expected_conditions.url_to_be(LOGIN_URL))
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        wait.until(expected_conditions.url_to_be(REGISTER_URL))

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        return { "email": email, "password": password }
