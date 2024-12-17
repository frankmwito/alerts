# Create a custom sequence of keyboard and mouse interactions using ActionChains.
# Automate a scenario involving clicking, typing, and scrolling using ActionChains.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

try:
    driver.get("https://www.toolsqa.com/")
    driver.maximize_window()
    
    WebDriverWait(driver, timeout= 5, poll_frequency= 1)
    
    wait = WebDriverWait(driver, timeout=5, poll_frequency=1)

    # Navigate to the 'Tutorials' section
    tutorials_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='navbar__tutorial-menu']")))
    driver.execute_script("arguments[0].click();", tutorials_menu)

    # Hover over 'QA Practices' menu
    frontend_test_automation = wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Front-End Testing Automation']")))
    actions = ActionChains(driver)
    actions.move_to_element(frontend_test_automation).perform()

    # Scroll and click 'TestProject'
    test_project_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='active']//a[@title='TestProject']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", test_project_link)
    actions.click(test_project_link).perform()

    # Right-click on an element (e.g., page content)
    element_to_context_click = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    actions.context_click(element_to_context_click).perform()

    # Use arrow keys and ENTER to interact with context menu
    actions.send_keys(Keys.ARROW_DOWN).perform()
    actions.send_keys(Keys.ARROW_DOWN).perform()
    actions.send_keys(Keys.ENTER).perform()
    
    WebDriverWait(driver, timeout= 10, poll_frequency= 1)

    print("Custom keyboard and mouse interactions completed successfully!")

except Exception as e:
    print("Error occurred:", e)

finally:
    driver.quit()
    
    
    