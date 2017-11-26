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

    box_menu = driver.find_element_by_id("box-apps-menu")
    driver.box_menu.find_elements_by_tag_name("li")

    for x in range(len(apps)):
            box_menu.find_elements_by_tag_name("li")[i]
            list = box_menu.find_elements_by_css_selector("ul li")

        for y in range(len(list)):
            box_menu = driver.find_element_by_id("box-apps-menu")
            box_menu.find_elements_by_tag_name("li")[x]
            driver.box_menu.find_elements_by_css_selector('ul li')[y].click()
            header_h1 = driver.find_element_by_tag_name("h1").text
            print(header_h1)