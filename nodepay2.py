from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

# Function to generate a random email
def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "example.com"]
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(domains)
    return f"{username}@{domain}"

# Function to generate a random password
def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

# Set up Selenium WebDriver (Chromium)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode (no GUI)
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Path to ChromiumDriver (update this path if necessary)
service = Service('/data/data/com.termux/files/home/chromedriver')
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open the website
    driver.get("https://app.depined.org/dashboard")
    time.sleep(5)  # Wait for the page to load

    # Generate random email and password
    email = generate_random_email()
    password = generate_random_password()

    print(f"Generated Email: {email}")
    print(f"Generated Password: {password}")

    # Locate the referral code input field (update the selector as needed)
    referral_input = driver.find_element(By.NAME, "referral_code")  # Replace with the correct element name or ID
    referral_input.send_keys("DE5I8I8fFzkNLu")

    # Locate and fill in the email field
    email_input = driver.find_element(By.NAME, "email")  # Replace with the correct element name or ID
    email_input.send_keys(email)

    # Locate and fill in the password field
    password_input = driver.find_element(By.NAME, "password")  # Replace with the correct element name or ID
    password_input.send_keys(password)

    # Submit the form
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Replace with the correct XPath
    submit_button.click()

    # Wait for the process to complete
    time.sleep(10)

    # Check if the referral was successful (update as needed)
    if "dashboard" in driver.current_url:
        print("Referral process completed successfully!")
    else:
        print("Referral process failed. Check the website structure or your script.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()