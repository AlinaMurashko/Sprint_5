from selenium.webdriver.support import expected_conditions
from urls import BASE_URL, LOGIN_URL, REGISTER_URL
from locators import HomePageLocators, LoginPageLocators, RegistrationPageLocators
from data import generate_random_email, get_test_password

class TestRegistration:
    def test_registration_provide_valid_credentials_registration_is_successful(self, driver, wait):
        email = generate_random_email()
        password = get_test_password()

        driver.get(BASE_URL)

        driver.find_element(*HomePageLocators.PERSONAL_ACCOUNT_LINK).click()
        wait.until(expected_conditions.url_to_be(LOGIN_URL))
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        wait.until(expected_conditions.url_to_be(REGISTER_URL))

        assert driver.current_url == REGISTER_URL

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        wait.until(expected_conditions.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL

    def test_registration_provide_unacceptable_password_registration_is_forbidden(self, driver, wait):
        email = generate_random_email()

        driver.get(BASE_URL)

        driver.find_element(*HomePageLocators.PERSONAL_ACCOUNT_LINK).click()
        wait.until(expected_conditions.url_to_be(LOGIN_URL))
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        wait.until(expected_conditions.url_to_be(REGISTER_URL))

        assert driver.current_url == REGISTER_URL

        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("short")

        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        wait.until(expected_conditions.url_to_be(REGISTER_URL))
        assert driver.current_url == REGISTER_URL
