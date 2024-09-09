import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Create a folder for downloading photos
folder_path = "PhotoGallery"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Task 1: Download Monthly Progress Report from the Documents menu
driver.get("https://labour.gov.in/")

# Find the "Documents" menu and click it (adjust the XPath or CSS selector as needed)
documents_menu = driver.find_element(By.LINK_TEXT, "Document")
documents_menu.click()

# Wait for the page to load and locate the Monthly Progress Report link
time.sleep(2)
progress_report_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Monthly Progress Report")
progress_report_link.click()

# Task 2: Download 10 photos from the Photo Gallery
driver.get("https://labour.gov.in/")  # Go back to the home page

# Click on the "Media" menu and access the "Photo Gallery" submenu
media_menu = driver.find_element(By.LINK_TEXT, "Media")
media_menu.click()

# Click on the Photo Gallery submenu
photo_gallery_link = driver.find_element(By.LINK_TEXT, "Photo Gallery")
photo_gallery_link.click()

# Wait for the gallery page to load
time.sleep(2)

# Find the first 10 photos on the page and download them
photos = driver.find_elements(By.TAG_NAME, "img")[:10]  # Adjust based on actual gallery structure
for idx, photo in enumerate(photos):
    photo_url = photo.get_attribute("src")
    photo_data = requests.get(photo_url).content
    with open(os.path.join(folder_path, f"photo_{idx+1}.jpg"), 'wb') as photo_file:
        photo_file.write(photo_data)

# Close the browser
driver.quit()

print("Downloaded 10 photos to the folder:", folder_path)