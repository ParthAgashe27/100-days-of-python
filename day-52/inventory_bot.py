from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoSuchElementException,
    TimeoutException,
)
from time import sleep
import random

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
WAIT_TIMEOUT = 10


class InventoryBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        })
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, WAIT_TIMEOUT)
        self.driver.get(URL)

    def login(self):
        username = self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        username.send_keys(USERNAME)

        password = self.driver.find_element(By.ID, value="password")
        password.send_keys(PASSWORD)

        login_button = self.driver.find_element(By.ID, value="login-button")
        login_button.click()

        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))

    def find_products(self):
        filter_dropdown = self.driver.find_element(By.CLASS_NAME, value="product_sort_container")
        select = Select(filter_dropdown)

        chosen_text = random.choice(select.options).text
        select.select_by_visible_text(chosen_text)
        print(f"Selected filter: {chosen_text}")

    def add_items(self, count=3):
        add_to_cart_buttons = self.driver.find_elements(By.CLASS_NAME, "btn_inventory")
        for button in add_to_cart_buttons[:count]:
            try:
                button.click()
            except ElementClickInterceptedException:
               
                self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
                sleep(0.3)
                button.click()
            sleep(0.5)

        shopping_cart = self.driver.find_element(By.CLASS_NAME, value="shopping_cart_link")
        shopping_cart.click()

        checkout_button = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

    def checkout(self, firstname, lastname, pincode):
        first_name = self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        first_name.send_keys(firstname)

        last_name = self.driver.find_element(By.ID, value="last-name")
        last_name.send_keys(lastname)

        zip_code = self.driver.find_element(By.ID, value="postal-code")
        zip_code.send_keys(pincode)

        continue_checkout_button = self.driver.find_element(By.ID, value="continue")
        continue_checkout_button.click()

        finish_button = self.wait.until(EC.element_to_be_clickable((By.ID, "finish")))
        finish_button.click()

    def confirmation(self):
        try:
            generate_the_order_pdf = self.wait.until(
                EC.element_to_be_clickable((By.ID, "generate-pdf-order"))
            )
            generate_the_order_pdf.click()
        except (NoSuchElementException, TimeoutException):
            print("PDF button not found/clickable — skipping PDF generation.")

        try:
            confirmation = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
            )
            print(confirmation.text)
        except TimeoutException:
            print("Confirmation header never showed up — checkout may have failed.")

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    bot = InventoryBot()
    try:
        bot.login()
        bot.find_products()
        bot.add_items(3)
        bot.checkout(firstname="light", lastname="shadow", pincode="162510")
        bot.confirmation()
    finally:
        bot.close()



