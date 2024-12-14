from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import pyperclip  # For clipboard operations (install with `pip install pyperclip`)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Navigate to a demo search page
    driver.get("https://www.google.com/")
    driver.maximize_window()
    
    # Wait for the search box to be available
    wait = WebDriverWait(driver, timeout=10)
    search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
    
    # Enter text into the search box
    search_box.send_keys("Selenium WebDriver automation")
    
    # Simulate Ctrl+A (select all text)
    search_box.send_keys(Keys.CONTROL + "a")
    
    # Simulate Ctrl+C (copy selected text)
    search_box.send_keys(Keys.CONTROL + "c")
    
    # Verify copied text using the clipboard
    copied_text = pyperclip.paste()
    if copied_text == "Selenium WebDriver automation":
        print("Text copied successfully:", copied_text)
    else:
        print("Text copy failed!")
    
    # Simulate Enter key to trigger search
    search_box.send_keys(Keys.ENTER)
    
    # Wait for the results page to load and confirm a result is visible
    wait.until(EC.visibility_of_element_located((By.ID, "search")))
    print("Search triggered successfully!")
    
except TimeoutException as e:
    print("An element was not found within the timeout period:", e)
except Exception as e:
    print("An error occurred:", e)
finally:
    driver.quit()
