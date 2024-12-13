# manage cookies
# adding cookies
# deleting cookies
# Reading cookies

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Navigate to URL and maximize window
    driver.get("https://practice-automation.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    
    # Add a cookie
    cookie = {"name": "test_cookie", "value": "cookie_value"}
    driver.add_cookie(cookie)
    print("Added cookie:", cookie)
    
    # Verify the cookie is added
    cookies = driver.get_cookies()
    print("Current cookies after addition:", cookies)
    if any(c['name'] == "test_cookie" for c in cookies):
        print("Verification passed: 'test_cookie' is present.")
    else:
        print("Verification failed: 'test_cookie' not found.")
    
    # Delete the specific cookie
    driver.delete_cookie("test_cookie")
    print("\nDeleted 'test_cookie'.")
    
    # Verify the cookie is deleted
    cookies = driver.get_cookies()
    if not any(c['name'] == "test_cookie" for c in cookies):
        print("Verification passed: 'test_cookie' has been removed.")
    else:
        print("Verification failed: 'test_cookie' is still present.")
    
    # Print all remaining cookies
    print("\nRemaining cookies:")
    for c in cookies:
        print(c)

    # Delete all cookies
    driver.delete_all_cookies()
    print("\nDeleted all cookies.")
    if not driver.get_cookies():
        print("Verification passed: All cookies have been deleted.")
    else:
        print("Verification failed: Some cookies remain.")

finally:
    driver.quit()

    
    
