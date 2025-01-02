from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class AssertionsTest():
    pass

def test_lambdatest_radio_button_demo_value():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
    
    driver.maximize_window()
    
    driver.find_element(By.XPATH,"//label[normalize-space()='Male']//input[@name='gender']").click()
    driver.find_element(By.XPATH, "//input[@value='15 - 50']").click()
    
    driver.find_element(By.XPATH, "//button[normalize-space()='Get values']").click()
    
    gender = driver.find_element(By.CSS_SELECTOR, ".genderbutton").text
    age_group = driver.find_element(By.CSS_SELECTOR, ".groupradiobutton").text
    
    print("Gender Object: \t", id(gender))
    print("Male Object: \t", id("Male"))
    assert gender == "Male", "Gender Is Not Correct"
    assert driver.title.__contains__("Selenium Grid Online")
    assert "49" in age_group, "Age Group Is Not Correct"