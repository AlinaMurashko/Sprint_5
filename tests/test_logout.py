from selenium.webdriver.support import expected_conditions
from urls import LOGIN_URL
from locators import LoginPageLocators, HomePageLocators, AccountPageLocators

class TestLogout:
    def test_logout_navigate_to_personal_account_and_click_logout_main_page_allows_to_login(self, driver, wait, registered_credentials):
        driver.get(LOGIN_URL)

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_credentials['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_credentials['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()


        wait.until(expected_conditions.presence_of_element_located(HomePageLocators.BURGER_TITLE))
        driver.find_element(*HomePageLocators.PERSONAL_ACCOUNT_LINK).click()

        wait.until(expected_conditions.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)).click()

        wait.until(expected_conditions.url_to_be(LOGIN_URL))
        assert driver.current_url == LOGIN_URL
        assert driver.find_element(*LoginPageLocators.EMAIL_INPUT).is_displayed()
