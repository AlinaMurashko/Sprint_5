from selenium.webdriver.support import expected_conditions
from urls import BASE_URL, LOGIN_URL, REGISTER_URL, FORGOT_PASSWORD_URL
from locators import HomePageLocators, RegistrationPageLocators, ForgotPasswordPageLocators

class TestLogin:
    def test_login_click_on_enter_personal_account_button_login_page_opens(self, driver, wait):
        driver.get(BASE_URL)

        driver.find_element(*HomePageLocators.ENTER_ACCOUNT_BUTTON).click()

        wait.until(expected_conditions.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL

    def test_login_click_on_personal_account_link_login_page_opens(self, driver, wait):
        driver.get(BASE_URL)

        driver.find_element(*HomePageLocators.ENTER_ACCOUNT_BUTTON).click()

        wait.until(expected_conditions.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL

    def test_login_navigate_to_registration_page_and_click_on_already_registered_link_login_page_opens(self, driver, wait):
        driver.get(REGISTER_URL)

        wait.until(expected_conditions.presence_of_element_located(RegistrationPageLocators.LOGIN_LINK))
        driver.find_element(*RegistrationPageLocators.LOGIN_LINK).click()

        wait.until(expected_conditions.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL

    def test_login_navigate_to_forgot_password_page_and_click_on_remembered_password_link_login_page_opens(self, driver, wait):
        driver.get(FORGOT_PASSWORD_URL)

        wait.until(expected_conditions.presence_of_element_located(ForgotPasswordPageLocators.LOGIN_LINK))
        driver.find_element(*ForgotPasswordPageLocators.LOGIN_LINK).click()

        wait.until(expected_conditions.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL
