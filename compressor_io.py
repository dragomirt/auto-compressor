import sys
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException


def inputData():
	try:
		if driver.find_element_by_css_selector('input[type="file"]'):
			driver.find_element_by_css_selector('input[type="file"]').send_keys(photos_folder + file)
	except NoSuchElementException as e:
		time.sleep(1)
		inputData()

def clickDownload():
	try:
		if driver.find_element_by_css_selector('#containerDownloaders .download'):
			driver.find_element_by_css_selector('#containerDownloaders .download').click()
			driver.get("https://compressor.io/compress")
	except Exception as e:
		time.sleep(1)
		clickDownload()

def addSlash(folder_str):
	if folder_str[-1] != '/' or folder_str[-1] != '\\':
		return folder_str + '/'


photos_folder = sys.argv[1]
photos_folder = addSlash(photos_folder)

download_folder = sys.argv[2]
files = os.listdir(photos_folder)
tooBigArr = []

options = webdriver.ChromeOptions() 
options.add_experimental_option("prefs", {
  "download.default_directory": download_folder,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
driver = webdriver.Chrome(options=options)

driver.get("https://compressor.io/compress")

for file in files:
	if file.endswith(".jpg"):
		if os.path.getsize(photos_folder + file) <= 10000000: # 10 MB
			inputData()
			clickDownload()
		else:
			tooBigArr.append(file)

print("Files too big for the compressor:")
print(tooBigArr)
print("Done!")