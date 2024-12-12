# nested frames

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open the target website
    driver.get("https://demoqa.com/nestedframes")
    driver.maximize_window()

    # **Switch to the parent frame**
    WebDriverWait(driver, 5).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1"))
    )
    parent_text = driver.find_element(By.TAG_NAME, "body").text
    print("Text in Parent Frame:", parent_text)

    # **Switch to the child frame inside the parent frame**
    child_frame = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(child_frame)
    child_text = driver.find_element(By.TAG_NAME, "p").text
    print("Text in Child Frame:", child_text)

    # Switch back to the main content
    driver.switch_to.default_content()

finally:
    # Quit the browser
    driver.quit()
