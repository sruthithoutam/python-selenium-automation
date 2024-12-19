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
driver.get(" https://www.target.com/ ")
driver.find_element(By.ID,"account-sign-in").click()
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
#verify the sign in target page
expected='Sign into your Target account'
actual=driver.find_element(By.XPATH,"//h1/span").text
assert expected == actual,f'expected{expected} did not match actually actual{actual}'

if expected and actual:
    print("SignIn page is successfully opened.")
else:
    print("SignIn page did not open correctly.")

sleep(2)






