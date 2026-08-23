from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

ACCOUNT_NAME = "YOUR_ACCOUNT_NAME" #public username - tomsmith 
ACCOUNT_PASSWORD = "YOUR_PASSWORD" # public password - SuperSecretPassword!
WEB_URL = "https://the-internet.herokuapp.com/login"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
})

driver = webdriver.Chrome(options=chrome_options)
driver.get(WEB_URL)

username = driver.find_element(By.ID, value="username")
username.send_keys(ACCOUNT_NAME)

sleep(1)

password = driver.find_element(By.ID, value="password")
password.send_keys(ACCOUNT_PASSWORD)

sleep(1)

login_button = driver.find_element(By.CLASS_NAME, value="radius")
login_button.click()


sleep(1)

driver.get("https://the-internet.herokuapp.com/windows")

# Store the original/base window handle
base_window = driver.window_handles[0]

new_window_link = driver.find_element(By.LINK_TEXT, value="Click Here")
print(new_window_link.get_attribute("outerHTML"))

driver.execute_script("arguments[0].click();", new_window_link)  # JS click instead

sleep(2)


new_window = driver.window_handles[1]

driver.switch_to.window(new_window)
print(driver.title)  

sleep(1)


driver.switch_to.window(base_window)
print(driver.title)  


driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Simple alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
sleep(1)
alert = driver.switch_to.alert   
print(alert.text)                
alert.accept()                   

# Confirm box (has OK and Cancel)
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
sleep(1)
alert = driver.switch_to.alert
alert.dismiss()                  #

# Prompt (has a text input)
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
sleep(1)
alert = driver.switch_to.alert
alert.send_keys("Parth")        
alert.accept()


driver.get("https://the-internet.herokuapp.com/entry_ad")
sleep(2)  

close_button = driver.find_element(By.CLASS_NAME, "modal-footer")

close_button.click()

driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
driver.find_element(By.XPATH, "//button[text()='Start']").click()

# Now the element takes a few seconds to appear


for i in range(10):  # max attempts
    try:
        result = driver.find_element(By.ID, "finish")
        print(result.text)
        break
    except NoSuchElementException:
        print("Not loaded yet, retrying...")
        sleep(1)
