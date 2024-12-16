# Automate a drag action chain

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service)


try: 
    driver.get("https://demoqa.com/dragabble")
    driver.maximize_window()
    
    driver.implicitly_wait(5)
    
    drag = driver.find_element(By.ID, "dragBox")
    actions = ActionChains(driver)
    
    actions.drag_and_drop_by_offset(drag, 30, 0)
    
    print("object dragged successfully")
    
finally:
    driver.quit()