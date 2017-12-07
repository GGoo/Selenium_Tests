import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_menu(driver):
    WebDriverWait(driver, 20)
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name('password').send_keys("admin")
    driver.find_element_by_css_selector("div.footer > button").click()
    WebDriverWait(driver,10).until(EC.title_is("My Store"))

    left_navigation = driver.find_element_by_id("box-apps-menu")
    list = left_navigation.find_elements_by_tag_name("li")

    for i in range(len(list)):
         left_navigation.find_elements_by_tag_name("li")[i]
         box_app_menu=left_navigation.find_elements_by_css_selector('ul li')

         for j in range(len(box_app_menu)):
             left_navigation = driver.find_element_by_id("box-apps-menu")
             driver.table.find_elements_by_tag_name("li")[i]
             left_navigation.find_elements_by_css_selector('ul li')[j].click()
             header_h1=driver.find_element_by_tag_name("h1").text
             print(header_h1)
