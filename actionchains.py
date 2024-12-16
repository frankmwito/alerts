# Automate drag-and-drop functionality between two elements.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Navigate to the webpage
    driver.get("https://demoqa.com/droppable")
    driver.maximize_window()
    WebDriverWait(driver, timeout= 5, poll_frequency= 1)
    
    
    source = driver.find_element(By.XPATH, "//div[@id='draggable']")
    target = driver.find_element(By.XPATH, "(//div[@id='droppable'])[1]")
    
    actions = ActionChains(driver)
    
    actions.drag_and_drop(source, target).perform()
    WebDriverWait(driver, timeout= 5, poll_frequency= 1)
    print("The drag and drop was succesful")    
    
finally:
    driver.quit()
    