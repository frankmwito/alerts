
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pytestmark = [pytest.mark.regression, pytest.mark.sanity]

@pytest.mark.integration
@pytest.mark.smoke
def test_lambdaa_ajax_form():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service = service)
    driver.get("https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo")
    driver.maximize_window()
    name = driver.find_element(By.ID,"title")
    name.send_keys("Pytest Tutorial")
    comment = driver.find_element(By.ID, "description")
    comment.send_keys("Lambda Selenium Playground")
    submit_button = driver.find_element(By.ID, "btn-submit")
    submit_button.click()
    request = driver.find_element(By.ID, "submit-control").text
    assert request.__contains__("Processing")

@pytest.mark.smoke
def test_e2e():
    print("End To End Test")
    
@pytest.mark.smoke   
def test_login():
    print("Log Into Application")
    
@pytest.mark.smoke
def test_logout():
     print("Log Out of Application")