from selenium.webdriver.common.by import By

class HomePageLocators:
    ENTER_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, ".//a[@href='/account']")
    CONSTRUCTOR_LINK = (By.XPATH, ".//a[.//text()='Конструктор']")
    LOGO = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')
    BUNS_TAB = (By.XPATH, ".//div[contains(@class,'tab_tab__1SPyG')][span[text()='Булки']]")
    SAUCES_TAB = (By.XPATH, ".//div[contains(@class,'tab_tab__1SPyG')][span[text()='Соусы']]")
    TOPPINGS_TAB = (By.XPATH, ".//div[contains(@class,'tab_tab__1SPyG')][span[text()='Начинки']]")
    BURGER_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, './/input[@name="name"]')
    PASSWORD_INPUT = (By.XPATH, './/input[@type="password"]')
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, ".//a[@href='/register']")
    FORGOT_PASSWORD_LINK = (By.XPATH, ".//a[@href='/forgot-password']")


class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, '(.//input[@name="name"])[1]')
    EMAIL_INPUT = (By.XPATH, '(.//input[@type="text"])[2]')
    PASSWORD_INPUT = (By.XPATH, './/input[@type="password"]')
    REGISTER_BUTTON = (By.CLASS_NAME, 'button_button_type_primary__1O7Bx')
    LOGIN_LINK = (By.XPATH, ".//a[@href='/login']")


class ForgotPasswordPageLocators:
    LOGIN_LINK = (By.XPATH, ".//a[@href='/login']")


class AccountPageLocators:
    PROFILE_LINK = (By.XPATH, ".//a[text()='Профиль']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
