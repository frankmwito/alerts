# capturing screenshots
# **capture the screenshot of a full webpage**
# Take a screenshot of a specific web element and save it as an image
# Automate capturing a screenshot when an exception occurs

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# setup the webdriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

# exception handling
try:
    # open the target website
    driver.get("https://demoqa.com/")
    driver.maximize_window()
    
    # locate the body of the webpage and take its screenshot
    body = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    body.screenshot(".\\test.png")
    
    # locate a specific webelement and take its screenshot
    training_img = driver.find_element(By.XPATH,"//img[@alt='Selenium Online Training']")
    training_img.screenshot("C:\\Users\\Gaming 15\\Downloads\\alerts\\test1.png")
    driver.get_screenshot_as_file("C:\\Users\\Gaming 15\\Downloads\\test2.png")
    
finally:
    # close the window
    driver.quit() 