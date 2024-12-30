from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_lambda_test():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        driver.get("https://www.lambdatest.com/selenium-playground/")
        print("Title: ", driver.title)
        assert "Selenium Grid Online" in driver.title, "Title does not match expected"
    finally:
        driver.quit()
