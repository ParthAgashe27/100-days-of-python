import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
})


URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL ="https://docs.google.com/forms/d/e/1FAIpQLScRI9YAbXJybCNtmN15BezDlP960X-iE_kkWVshT32XasBKxA/viewform"

driver = webdriver.Chrome(options=chrome_options)
driver.get(FORM_URL)


response = requests.get(URL)

soup = BeautifulSoup(response.content, "html.parser")

listings = soup.find_all("article", attrs={"data-test": "property-card"})

links = [listing.find("a", attrs={"data-test": "property-card-link"})["href"] for listing in listings]
prices = [listing.find("span", attrs={"data-test": "property-card-price"}).text for listing in listings]
cleaned_prices = [price.split("+")[0].split("/")[0].strip() for price in prices]
address = [listing.find("address", attrs={"data-test": "property-card-addr"}).text for listing in listings]
cleaned_addresses = [" ".join(addr.replace("|", "").split()) for addr in address]

print(links[:3])
print(cleaned_prices[:3])
print(cleaned_addresses[:3])

# Find each question's container by its label text, then locate the input inside it
address_input = driver.find_element(
    By.XPATH,
    "//div[contains(., \"What's the address of your property?\")]//input"
)

for link, price, addr in zip(links, cleaned_prices, cleaned_addresses):
    driver.get(FORM_URL)
    sleep(1)

    inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    address_input, price_input, link_input = inputs[0], inputs[1], inputs[2]

    address_input.send_keys(addr)
    price_input.send_keys(price)
    link_input.send_keys(link)

    submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
    submit_button.click()

    sleep(1)
