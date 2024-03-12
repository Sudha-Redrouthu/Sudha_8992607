# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()
driver.maximize_window()
# Navigating to the CIBC banking home page
driver.get("https://www.cibc.com/")
time.sleep(4)

# Selecting investments option from the home page
Investments = driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/div/nav/section/ul/li[5]/a")
Investments.click()
time.sleep(5)

# Scrolling down
driver.execute_script("scroll(0,1000)")
time.sleep(3)

# Selecting explore more option
Explore = driver.find_element("xpath","(//div[contains(@class,'multi-cta')])[2]")
Explore.click()
time.sleep(5)

# Scroll down
driver.execute_script("scroll(0,1500)")
time.sleep(3)

# Click on Retirement Plan
Retirement_plan = driver.find_element("xpath","(//div[contains(@class,'callout base parbase')])[12]")
Retirement_plan.click()
time.sleep(5)

# Scroll down
driver.execute_script("scroll(0,1400)")
time.sleep(3)

# Opening Retirement plan site
driver.get("https://www.cibc.com/en/personal-banking/investments/retirement-planning/rrsp-options.html")
time.sleep(5)

# Scroll down
driver.execute_script("scroll(0,1400)")
time.sleep(3)

driver.find_element("xpath","//span[@class='nextactionctaText'][contains(text(),'Need to meet?')]").click()
time.sleep(3)

# Closing the webdriver
driver.close()