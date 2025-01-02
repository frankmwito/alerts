from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_lambdatest_simple_form_demo():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    driver.find_element(By.XPATH, "//input[@id='user-message']").send_keys("Pytest is a test framework")
    
    driver.find_element(By.ID, "showInput").click()
    
    message = driver.find_element(By.ID, "message").text
    
    
    assert message == "Pytest is a test framework"