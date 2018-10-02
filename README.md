# auto-compressor
Automation for compressor.io for bulk compression

## Requirements:
+ Python 3.x
+ Selenium
+ Chrome Webdriver ( Get it here: http://chromedriver.chromium.org/downloads )
+ Google Chrome browser

## Install:
##### Unix
```bash
	pip3 install selenium
	wget https://chromedriver.storage.googleapis.com/2.42/chromedriver_mac64.zip
	unzip chromedriver_mac64.zip
	sudo mv ./chromedriver /usr/local/bin
	sudo chmod +x /usr/local/bin/chromedriver
```

##### Windows
```bash
	pip3 install selenium
	# Extract the chromedriver.exe from https://chromedriver.storage.googleapis.com/2.42/chromedriver_win32.zip
	# Paste it into a dedicated folder
	# Add the folder to PATH
```

## Using the script:
```bash
	python3 compressor_io.py <absolute path to the imgs folder> <absolute path to the download folder>
	# Ex. python3 compressor_io.py C:\workspace\imgs C:\workspace\compressed
```
