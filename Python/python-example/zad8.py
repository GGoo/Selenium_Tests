import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def login(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("username")
    driver.find_element_by_name('password').send_keys("admin")
    driver.find_element_by_css_selector("div.footer > button").click()
    WebDriverWait(driver,10).until(EC.title_is("My Store"))

def checking_nr_of_stickers(driver):
    