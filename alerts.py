# handling alerts

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Navigate to the test website
    driver.get("https://demoqa.com/alerts")
    driver.maximize_window()

    # **Scenario 1: Handle Simple Alert**
    driver.find_element(By.ID, "alertButton").click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Simple Alert Text:", alert.text)
    alert.accept()

    # **Scenario 2: Handle Confirmation Alert**
    driver.find_element(By.ID, "confirmButton").click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Confirmation Alert Text:", alert.text)
    alert.dismiss()

    # **Scenario 3: Handle Prompt Alert**
    driver.find_element(By.ID, "promtButton").click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Frankie")
    print("Prompt Alert Text:", alert.text)
    alert.accept()

    # **Scenario 4: Handle Timer Alert**
    driver.find_element(By.ID, "timerAlertButton").click()  # Corrected .click() usage
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("Timer Alert Text:", alert.text)
    alert.accept()

finally:
    # Close the browser
    driver.quit()

    