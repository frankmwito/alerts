from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
import math

# Test for two input fields
@pytest.mark.parametrize("num1, num2, expected_total", [("25", "25", "50"), ("10", "10", "20"), ("30", "40", "70")])
def test_lambdatest_two_input_fields(num1, num2, expected_total):
    # Set up the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    driver.maximize_window()
    
    # Find the input fields
    driver.find_element(By.ID, "sum1").send_keys(num1)
    driver.find_element(By.ID, "sum2").send_keys(num2)
    driver.find_element(By.XPATH, "//button[normalize-space()='Get Sum']").click()
    
    # Retrieve the actual total
    actual_total = driver.find_element(By.ID, "addmessage").text
    
    # Assertion
    assert actual_total == expected_total, f"Actual and Expected Total Do Not Match: {actual_total} != {expected_total}"
    driver.quit()

# Test for raising base to a power
@pytest.mark.parametrize("base", [1, 2, 3])
@pytest.mark.parametrize("exponent", [4, 5])
def test_raising_base_to_power(base, exponent):
    # Calculate the result
    result = base ** exponent
    # Compare with math.pow
    assert result == math.pow(base, exponent), f"Failed for base {base} and exponent {exponent}"
