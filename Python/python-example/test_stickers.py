import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_sticker(driver):
    driver.get("http://localhost/litecart")
    WebDriverWait(driver, 10)
    ducks = driver.find_elements_by_css_selector('li.product')
    for duck in ducks:
        sticker = duck.find_elements_by_css_selector('div.sticker')
        assert len(sticker) == 1



