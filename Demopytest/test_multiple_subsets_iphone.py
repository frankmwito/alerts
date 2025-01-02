from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def test_search_lambda_ecommerce():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.get("https://ecommerce-playground.lambdatest.io/")
    driver.maximize_window()
    
    search_pad = driver.find_element(By.XPATH, "//input[@placeholder='Search For Products']")
    search_pad.send_keys("iphone")
    
    search = driver.find_element(By.XPATH, "//button[normalize-space()='Search']")
    search.click()
    
    search_value = driver.find_element(By.XPATH, "//h1[@class='h4']").text
    
    assert "iphone" in search_value