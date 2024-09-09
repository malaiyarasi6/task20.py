from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the CoWIN homepage
driver.get("https://www.cowin.gov.in/")

# Wait for the page to load completely
time.sleep(3)

# Find and click the FAQ and Partners anchor tag (replace with the correct XPath/Selector)
faq_link = driver.find_element(By.LINK_TEXT, "FAQ")
partners_link = driver.find_element(By.LINK_TEXT, "Partners")

# Open both links in new windows
faq_link.send_keys(webdriver.common.keys.Keys.CONTROL + webdriver.common.keys.Keys.RETURN)
partners_link.send_keys(webdriver.common.keys.Keys.CONTROL + webdriver.common.keys.Keys.RETURN)

# Get window handles (IDs) of the opened windows
windows = driver.window_handles
for window in windows:
    print(f"Window ID: {window}")

# Switch to the newly opened windows and close them
for window in windows[1:]:
    driver.switch_to.window(window)
    driver.close()

# Switch back to the original window (home page)
driver.switch_to.window(windows[0])

# Close the driver
driver.quit()
