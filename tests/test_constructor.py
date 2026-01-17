import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestConstructor:

    @pytest.mark.parametrize(
        'tab_name',
        [
            'Булки', 'Соусы', 'Начинки'
        ]
    )
    def test_constructor_click_on_burger_part_tab_tab_becomes_active(self, target_url, tab_name):
        driver = webdriver.Chrome()

        driver.get(target_url)

        tab_element = driver.find_element(By.XPATH, f'//div[contains(@class,"tab_tab__1SPyG")][span[text()="{tab_name}"]]')

        tab_element.click()

        WebDriverWait(driver, 3)

        assert 'tab_tab_type_current__2BEPc' in tab_element.get_attribute('class')

        driver.quit()
