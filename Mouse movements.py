# Automate hovering over a dropdown menu and selecting an item.
# Write a script to perform a right-click on a web element and select an option from the context menu.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Navigate to the webpage
    driver.get("https://www.toolsqa.com/")
    driver.maximize_window()

    wait = WebDriverWait(driver, timeout=10, poll_frequency=2)

    # Hover over the dropdown menu
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='navbar__tutorial-menu']"))).click()
    actions = ActionChains(driver)
    
    # Wait for and click on a specific menu item
    menu_item = wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='QA Practices']")))
    actions.move_to_element(menu_item).perform()

    # Wait for a sub-menu item and click on it
    submenu_item = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul[class='active'] a[title='ISTQB Preparation']")))
    submenu_item.click()

    # Wait for a specific element to right-click on
    content_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.col.flex-grow-1.article-body__content')))
    actions.context_click(content_element).perform()

    # Navigate the context menu using keyboard shortcuts
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN).perform()  # Navigate to the first option
    actions.send_keys(Keys.ARROW_DOWN).perform()  # Navigate to the second option
    actions.send_keys(Keys.ENTER).perform()       # Select the highlighted option

    print("Dropdown and context menu actions performed successfully.")
    
except TimeoutException as e:
    print("Timeout occurred while waiting for elements:", e)
except Exception as e:
    print("An error occurred:", e)
finally:
    driver.quit()
