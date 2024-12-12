# explicit waits
# implicit waits; handle dynamic web elements
# fluent waits

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://demoqa.com/")
    driver.maximize_window()
    
    # **Implicit Wait**
    driver.implicitly_wait(5)
    
    # Locate an element and click on it using JavaScript
    button = driver.find_element(By.XPATH, "//img[@alt='Selenium Online Training']")
    driver.execute_script("arguments[0].click();", button)  # Corrected JavaScript click syntax
    
    # **Fluent Wait**
    fluent_wait = WebDriverWait(driver, timeout=10, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
    fluent_element = fluent_wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Go To Registration']")))
    print("Fluent Wait: Element is visible.")
    
    # **Explicit Wait**
    explicit_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Go To Registration']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", explicit_element)
    print("Explicit Wait: Element is visible.")

except TimeoutException:
    print("TimeoutException: The element was not found within the specified time.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
