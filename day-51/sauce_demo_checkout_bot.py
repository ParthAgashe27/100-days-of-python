import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from time import sleep

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
})


driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

sleep(2)

username = driver.find_element(By.ID, value="user-name")
username.send_keys(USERNAME)

sleep(1)

password = driver.find_element(By.ID, value="password")
password.send_keys(PASSWORD)

login_button = driver.find_element(By.ID, value="login-button")
login_button.click()

filter_dropdown = driver.find_element(By.CLASS_NAME, value="product_sort_container")
select = Select(filter_dropdown)

options = select.options
chosen = random.choice(options)
chosen_text = chosen.text  # grab text NOW, while element is still valid

select.select_by_visible_text(chosen_text)  # this may invalidate 'chosen'

print(f"Selected filter: {chosen_text}")  # use the saved string, not chosen.text again
sleep(1)


add_to_cart_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
for button in add_to_cart_buttons[:3]:
    button.click()
    sleep(0.5)

shopping_cart = driver.find_element(By.CLASS_NAME, value="shopping_cart_link")
shopping_cart.click()

checkout_button = driver.find_element(By.ID, value="checkout")
checkout_button.click()

#checkout - info

FIRST_NAME = input("Enter your first name : ")
LAST_NAME = input("Enter your last name: ")
ZIPCODE = input("Enter your Zip/Postal code: ")

first_name = driver.find_element(By.ID, value="first-name")
first_name.send_keys(FIRST_NAME)

last_name = driver.find_element(By.ID, value="last-name")
last_name.send_keys(LAST_NAME)

zip_code = driver.find_element(By.ID, value="postal-code")
zip_code.send_keys(ZIPCODE)

continue_checkout_button = driver.find_element(By.ID, value="continue")
continue_checkout_button.click()

finish_button = driver.find_element(By.ID, value="finish")
finish_button.click()

generate_the_order_pdf = driver.find_element(By.ID, value="generate-pdf-order")
generate_the_order_pdf.click()


sleep(1)
confirmation = driver.find_element(By.CLASS_NAME, "complete-header")
print(confirmation.text)  # should print "THANK YOU FOR YOUR ORDER"

