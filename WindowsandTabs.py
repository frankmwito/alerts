# Automate opening multiple tabs, switching between them, and closing specific ones.
# Write a script to switch between multiple browser windows and verify their titles.
# Handle pop-ups in a new tab and return to the main tab after completing operations.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Open the main page
    driver.get("https://www.google.com")
    driver.maximize_window()
    main_window = driver.current_window_handle
    print(f"Main window handle: {main_window}")
    
    # Step 2: Open a new tab and switch to it
    driver.execute_script("window.open('https://www.selenium.dev', '_blank');")
    time.sleep(2)
    window_handles = driver.window_handles
    print(f"Window handles: {window_handles}")
    
    # Switch to the new tab
    driver.switch_to.window(window_handles[1])
    print(f"Switched to tab with title: {driver.title}")

    # Step 3: Perform an action on the new tab
    driver.find_element(By.LINK_TEXT, "Downloads").click()
    time.sleep(2)

    # Step 4: Open another tab and switch to it
    driver.execute_script("window.open('https://demoqa.com/browser-windows', '_blank');")
    time.sleep(2)
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[2])
    print(f"Switched to new tab with title: {driver.title}")

    # Step 5: Handle pop-ups in the new tab
    driver.find_element(By.ID, "tabButton").click()  # Opens a new window
    time.sleep(2)
    all_windows = driver.window_handles
    print(f"All windows after pop-up: {all_windows}")

    # Switch to the pop-up window
    for window in all_windows:
        if window != main_window and window not in window_handles:
            driver.switch_to.window(window)
            print(f"Switched to pop-up with title: {driver.title}")
            driver.close()  # Close the pop-up
            print("Closed the pop-up window")
    
    # Return to the main tab
    driver.switch_to.window(main_window)
    print(f"Back to the main window with title: {driver.title}")

finally:
    driver.quit()