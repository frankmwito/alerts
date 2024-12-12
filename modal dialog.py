# modal dialogs

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# setup the webdriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

# exception handling
try:
    # open the target website
    driver.get("https://demoqa.com/modal-dialogs")
    driver.maximize_window()
    
    # locate the small_dialog button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "showSmallModal"))).click()
    text_1 = driver.find_element(By.CLASS_NAME, "modal-body").text
    print("Small modal dialog body:", text_1)
    
    driver.implicitly_wait(3)
    # locate and click close small_dialog button
    driver.find_element(By.ID, "closeSmallModal").click()
    driver.implicitly_wait(3)
    
    
    driver.implicitly_wait(3)
    # locate the large_dialog button
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, "showLargeModal"))).click()
    text_1 = driver.find_element(By.TAG_NAME, "p").text
    print("Large modal dialog body:", text_1)
    
    driver.implicitly_wait(3)
    # locate and click close large_dialog button
    driver.find_element(By.ID, "closeLargeModal").click()
    driver.implicitly_wait(3)
    
    
finally:
    driver.quit()