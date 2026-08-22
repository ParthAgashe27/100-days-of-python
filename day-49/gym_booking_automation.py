import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

ACCOUNT_EMAIL = "hhhdujrivfgh3423t2ufguqwgru@test.com"  # The email you registered with
ACCOUNT_PASSWORD = "gfusdfiui4jk5264781[;[/;wkvyfy3"      # The password you used during registration
GYM_URL = "https://appbrewery.github.io/gym/"

def retry(func, retries=7, description=None):
    for attempt in range(retries):
        try:
            result = func()
            return result  # success, stop retrying
        except Exception as e:
            print(f"Attempt {attempt + 1} failed for {description}: {e}")
    print(f"Gave up after {retries} attempts: {description}")
    return None  # or raise, depending on how you want failures handled

booked_count = 0
waitlist_count = 0
already_count = 0

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)
wait = WebDriverWait(driver, 10)


sleep(2)
def login():
    try:
        initial_button = driver.find_element(By.CLASS_NAME, value="Home_heroButtons__w38oP")
        initial_button.click()
        sleep(2)
    except NoSuchElementException:
        pass  

    user_email = driver.find_element(By.CSS_SELECTOR, value="#email-input.Login_input__RLJo3")
    user_email.send_keys(ACCOUNT_EMAIL)

    sleep(2)

    user_pass = driver.find_element(By.CSS_SELECTOR, value="#password-input.Login_input__RLJo3")
    user_pass.send_keys(ACCOUNT_PASSWORD)

    sleep(1)

    login_button = driver.find_element(By.CSS_SELECTOR, value="#submit-button.Login_submitButton__tJFna ")
    login_button.click()

    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

def book_class(card, booking_button, original_text):
    booking_button.click()
    sleep(1)  # give the page a moment to update
    
    new_text = booking_button.text
    if new_text == original_text:
        raise Exception("Booking click didn't register — button text unchanged")

retry(login, description="login")


processed_classes = []

for day in ["tue", "thu"]:
    try:
        day_group = driver.find_element(By.CSS_SELECTOR, value=f"div[id^='day-group-{day}']")
        class_cards = day_group.find_elements(By.CSS_SELECTOR, value="div[id^='class-card-']")
    except NoSuchElementException:
        print(f"No classes found for {day} in this window, skipping.")
        continue

    for card in class_cards:
        time_element = card.find_element(By.CSS_SELECTOR, value="p[id^='class-time-']")
        booking_button = card.find_element(By.CSS_SELECTOR, value="button[id^='book-button-']")

        if "6:00" in time_element.text:
            class_name = card.find_element(By.CSS_SELECTOR, value="[id^='class-name-']")
            card_id = card.get_attribute("id")  # e.g. "class-card-spin-2026-08-25-1800"
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            cards = card_id.split("-")

            original_text = booking_button.text
            class_info = f"{class_name.text} on {f"{cards[5]}/{cards[4]}/{cards[3]}"}"

            if original_text == "Booked":
                print(f"✓ Already Booked: {class_info}")
                already_count += 1
                processed_classes.append(f"[Booked] {class_info}")
                

            elif original_text == "Waitlisted":
                print(f"✓ Already on waitlist: {class_info}")
                already_count += 1
                processed_classes.append(f"[Waitlisted] {class_info}")
                

            elif original_text == "Book Class":
                retry(lambda: book_class(card, booking_button, original_text), description=f"booking {class_name.text}")
                print(f"✓ Booked: {class_info}")
                booked_count += 1
                processed_classes.append(f"[New Booking] {class_info}")

            elif original_text == "Join Waitlist":
                retry(lambda: book_class(card, booking_button, original_text), description=f"waitlisting {class_name.text}")
                print(f"✓ Joined waitlist for: {class_info}")
                waitlist_count += 1
                processed_classes.append(f"[New Waitlist] {class_info}")


total_booked =  booked_count + waitlist_count + already_count 

# print(f"--- BOOKING SUMMARY ---\nClasses booked: {booked_count}\nWaitlists joined: {waitlist_count}\nAlready booked/waitlisted: {already_count}\nTotal Tuesday 6pm classes processed: {total}")

# print("\n--- DETAILED CLASS LIST ---")
# for class_detail in processed_classes:
#     print(f"  • {class_detail}")

print(f"--- Total Tuesday/Thursday 6pm classes: {total_booked} ---\n--- VERIFYING ON MY BOOKINGS PAGE ---")

my_bookings_link = driver.find_element(By.ID, "my-bookings-link")
my_bookings_link.click()

sleep(2)


confirmed_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='booking-card-']")
waitlist_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='waitlist-card-']")

found_count = 0

for card in confirmed_cards:
    name = card.find_element(By.CSS_SELECTOR, "h3[id^='booking-class-name-']").text
    when = card.find_element(By.CSS_SELECTOR, "p").text
    print("Confirmed:", name, "|", when)
    found_count += 1

for card in waitlist_cards:
    name = card.find_element(By.CSS_SELECTOR, "h3[id^='waitlist-class-name-']").text
    when = card.find_element(By.CSS_SELECTOR, "p").text
    print("Waitlist:", name, "|", when)
    found_count += 1

print("\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {found_count} bookings")

if found_count == total_booked:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {found_count - total_booked} bookings")

