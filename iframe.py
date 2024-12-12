# iframe scripts

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open the target website
    driver.get("https://demoqa.com/frames")
    driver.maximize_window()
    driver.refresh()

    # Switch to the first frame
    WebDriverWait(driver, 5).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1"))
    )
    title_1 = driver.find_element(By.ID, "sampleHeading").text
    print("Title from frame1:", title_1)

    # Switch back to the main content
    driver.switch_to.default_content()

    # Switch to the second frame
    WebDriverWait(driver, 5).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "frame2"))
    )
    title_2 = driver.find_element(By.ID, "sampleHeading").text
    print("Title from frame2:", title_2)

finally:
    # Close the browser
    driver.quit()
