import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()


# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get("https://www.amazon.com/")
driver.implicitly_wait(20)
driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
driver.find_element(By.ID, "createAccountSubmit").click()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, "[class*='a-icon a-icon-logo']")
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, "[class*='a-spacing-small']")
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
driver.find_element(By.CSS_SELECTOR, "#ap_email")
driver.find_element(By.CSS_SELECTOR,"#ap_password")
driver.find_element(By.CSS_SELECTOR,"#ap_password_check")
driver.find_element(By.CSS_SELECTOR,"#continue").click()
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")
driver.find_element(By.CSS_SELECTOR,".a-link-emphasis")
time.sleep(5)
