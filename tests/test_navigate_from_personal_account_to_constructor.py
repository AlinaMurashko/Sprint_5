import pytest
from selenium.webdriver.support import expected_conditions
from urls import LOGIN_URL
from locators import LoginPageLocators, HomePageLocators, AccountPageLocators

class TestNavigateFromPersonalAccountToConstructor:
    @pytest.mark.parametrize(
        'tested_locator',
        [
            HomePageLocators.CONSTRUCTOR_LINK,
            HomePageLocators.LOGO
        ]
    )
    def test_navigate_from_personal_account_page_to_home_page(self, driver, wait, registered_credentials, tested_locator):
        driver.get(LOGIN_URL)

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_credentials['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_credentials['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        wait.until(expected_conditions.presence_of_element_located(HomePageLocators.BURGER_TITLE))
        driver.find_element(*HomePageLocators.PERSONAL_ACCOUNT_LINK).click()
        wait.until(expected_conditions.presence_of_element_located(AccountPageLocators.LOGOUT_BUTTON))

        driver.find_element(*tested_locator).click()
        wait.until(expected_conditions.presence_of_element_located(HomePageLocators.BURGER_TITLE))

        assert driver.find_element(*HomePageLocators.BURGER_TITLE).is_displayed()
