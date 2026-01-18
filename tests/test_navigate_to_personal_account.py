from selenium.webdriver.support import expected_conditions
from urls import LOGIN_URL, ACCOUNT_PROFILE_URL
from locators import LoginPageLocators, HomePageLocators, AccountPageLocators

class TestNavigateToPersonalAccount:
    def test_login_succesfully_click_on_personal_account_link_personal_account_page_opens(self, driver, wait, registered_credentials):
        driver.get(LOGIN_URL)

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_credentials['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_credentials['password'])

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        wait.until(expected_conditions.presence_of_element_located(HomePageLocators.BURGER_TITLE))

        driver.find_element(*HomePageLocators.PERSONAL_ACCOUNT_LINK).click()

        wait.until(expected_conditions.presence_of_element_located(AccountPageLocators.LOGOUT_BUTTON))

        assert driver.current_url == ACCOUNT_PROFILE_URL
