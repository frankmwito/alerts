# Sending Keyboard inputs
# Automate filling a form using keyboard inputs only.
# Simulate keyboard shortcuts like Ctrl+A and Ctrl+C in a text field.
# Handle a scenario where pressing Enter triggers a search operation.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Navigate to the webpage
    driver.get("https://www.instagram.com/")
    driver.maximize_window()
    
    driver.implicitly_wait(5)
    
    # Simulate form filling
    username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    username.send_keys("Daviddeinhard@gmail.com")
    
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.send_keys("wenfriuber")
    
    submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit.click()
    
    driver.implicitly_wait(5)
    
    # Wait for the error message to appear
    try:
        wait = WebDriverWait(driver, timeout=10, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
        error_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@role='alert']")))  # Adjust locator as needed
        error_element.screenshot(".\\password_error.png")
        print("Error screenshot captured.")
    except TimeoutException:
        print("Error message not found within the timeout. Capturing full-page screenshot.")
        driver.save_screenshot(".\\full_page_screenshot.png")
    
finally:
    driver.quit()

