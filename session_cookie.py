# using cookies to maintain a session

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Start a session and retrieve a session cookie
    driver.get("https://practice-automation.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    
    # Retrieve a cookie (assuming a session-related cookie exists)
    session_cookie = driver.get_cookie("session_id")  # Replace "session_id" with the actual cookie name if known
    
    if session_cookie:
        print("Session cookie retrieved:", session_cookie)
    else:
        print("No session cookie found. Exiting.")
        driver.quit()
        exit()
    
    # Quit the first browser session
    driver.quit()
    
    # Step 2: Start a new browser session and restore the session
    driver = webdriver.Chrome(service=service)
    driver.get("https://practice-automation.com/")
    
    # Add the previously saved cookie
    driver.add_cookie(session_cookie)
    print("Session cookie added to the new browser session.")
    
    # Refresh the browser to load the session
    driver.refresh()
    
    # Verification (Optional): Check if a specific element indicates a successful session
    # Example: Look for a logged-in user element or session-dependent page content
    # Use driver.find_element(By.XPATH, "element_xpath") to verify
    print("Session restored successfully!")
    
finally:
    driver.quit()
