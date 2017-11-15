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
    driver.find_element_by_name("username").send_keys("username");
    driver.find_element_by_xpath("//*[@id='box-login']/form/div[1]/table/tbody/tr[2]/td[2]/span/input").send_keys("admin");
    driver.find_element_by_selector("#box-account-login > div > form > table > tbody > tr:nth-child(4) > td > span > button:nth-child(1)").click();
    driver.find_element_by_xpath("//*[@id='box-login']/form/div[1]/table/tbody/tr[3]/td[2]/label/input").click();
    WebDriverWait(driver,10).until(EC.title_is("My Store"));