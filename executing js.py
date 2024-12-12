# Executing javascript
# Use JavaScriptExecutor to scroll to a specific element on a page.
# Write a script to retrieve a webpage's title using JavaScriptExecutor.
# Inject custom JavaScript to modify an element's style and verify the change.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open the target website
    driver.get("https://demoqa.com/")
    driver.maximize_window()
    driver.implicitly_wait(4)

    # Scroll to a specific element using JavaScriptExecutor
    element_to_scroll_to = driver.find_element(By.XPATH, "//div[@class='category-cards']/div[3]")
    driver.execute_script("arguments[0].scrollIntoView(true);", element_to_scroll_to)
    print("Scrolled to the element.")
    
    driver.execute_script("arguments[0].click;",element_to_scroll_to)
    driver.back()
    driver.implicitly_wait(5)
    # Retrieve the webpage's title using JavaScriptExecutor
    page_title = driver.execute_script("return document.title;")
    print("Page Title (via JavaScriptExecutor):", page_title)

    # Modify an element's style using custom JavaScript and verify the change
    driver.execute_script("arguments[0].style.border='3px solid red';", element_to_scroll_to)
    print("Added a red border to the element.")

    # Wait to visually verify the change (optional)
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='category-cards']/div[3]"))
    )
    driver.implicitly_wait(10)
    
    element_to_scroll_to1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]')
    driver.execute_script("arguments[0].scrollIntoView(true);", element_to_scroll_to)
    print("Scrolled to element 1")
    
    driver.execute_script("arguments[0].style.color = 'yellow';", element_to_scroll_to1)
    print("The style color has been modified")

finally:
    # Close the browser
    driver.quit()
