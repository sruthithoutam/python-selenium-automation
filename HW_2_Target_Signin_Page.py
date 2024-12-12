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

# open the url
driver.get(" https://www.target.com/ ")
driver.find_element(By.ID,"account-sign-in").click()
driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()
driver.find_elements(By.NAME,"Sign into your Target account")
driver.find_elements(By.NAME,"Sign in with password")

sleep(5)