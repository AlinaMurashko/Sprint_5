import pytest
from selenium.webdriver.support import expected_conditions
from urls import BASE_URL
from locators import HomePageLocators

class TestConstructor:
    @pytest.mark.parametrize(
        'tab_locator',
        [
            HomePageLocators.BUNS_TAB,
            HomePageLocators.SAUCES_TAB,
            HomePageLocators.TOPPINGS_TAB
        ]
    )
    def test_constructor_click_on_burger_part_tab_tab_becomes_active(self, driver, wait, tab_locator):
        driver.get(BASE_URL)

        tab_element = driver.find_element(*tab_locator)
        tab_element.click()

        wait.until(expected_conditions.visibility_of(tab_element))

        assert 'tab_tab_type_current__2BEPc' in tab_element.get_attribute('class')
