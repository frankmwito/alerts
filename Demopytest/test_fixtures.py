import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
@pytest.fixture()
def setup_teardown():
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    driver.find_element(By.ID, "input-email").send_keys("mfranklyne039@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("1234567890")
    driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
    print("login")
    yield
    driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
    print("Logout")
    
def test1_order_history_title(setup_teardown):
    driver.find_element(By.PARTIAL_LINK_TEXT, "Order Histo").click()
    assert driver.title == "Order History"
    print("Test 1 Is Complete")
    
    