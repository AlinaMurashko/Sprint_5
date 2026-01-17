import pytest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def target_url():
    return 'https://stellarburgers.education-services.ru'

@pytest.fixture
def email():
    names = ['alina', 'galina', 'polina', 'albina']
    surnames = ['murashko', 'murashkova', 'murashina']
    stream = '37'
    random_number = random.randint(100, 999)
    return f'{random.choice(names)}_{random.choice(surnames)}_{stream}_{random_number}@yandex.ru'

@pytest.fixture
def password():
    return 'securePassword'

@pytest.fixture
def registered_credentials(target_url, account_link_locator, registration_link_locator, email, password):
        driver = webdriver.Chrome()

        driver.get(target_url)

        driver.find_element(By.XPATH, account_link_locator).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, registration_link_locator)))

        driver.find_element(By.XPATH, registration_link_locator).click()

        for element in driver.find_elements(By.XPATH, './/input[@name="name"]'):
            element.send_keys(email)

        driver.find_element(By.XPATH, './/input[@type="password"]').send_keys(password)

        driver.find_element(By.CLASS_NAME, 'button_button_type_primary__1O7Bx').click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, registration_link_locator)))

        driver.quit()

        return { "email": email, "password": password }

@pytest.fixture
def account_link_locator():
    return ".//a[@href='/account']"

@pytest.fixture
def registration_link_locator():
    return ".//a[@href='/register']"

@pytest.fixture
def login_link_locator():
    return ".//a[@href='/login']"

@pytest.fixture
def forgot_password_link_locator():
    return ".//a[@href='/forgot-password']"

@pytest.fixture
def enter_personal_account_button_locator():
    return ".//button[text()='Войти в аккаунт']"

@pytest.fixture
def login_input_locator():
    return './/input[@name="name"]'

@pytest.fixture
def password_input_locator():
    return './/input[@type="password"]'

@pytest.fixture
def logout_button_locator():
    return ".//button[text()='Выход']"

@pytest.fixture
def register_button_class_name():
    return 'button_button_type_primary__1O7Bx'