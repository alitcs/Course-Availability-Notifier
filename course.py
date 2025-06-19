import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# Import from telephony API (example Twilio import statement included)
from twilio.rest import Client

# Telephony API credentials
account_sid = '' # Enter account sid
auth_token = '' # Enter authorization token
from_number = '' # Enter from number, format: +1234567890
to_number = '' # Enter to number, format: +1234567890


chrome_driver_path = r"" # Enter path to your ChromeDriver
profile_path = r"" # Enter path to chrome profile
profile_name = r"" # Enter profile name

# Set up Chrome options to use existing profile
options = Options()
options.add_argument(f"user-data-dir={profile_path}")
options.add_argument(f"profile-directory={profile_name}")

login_url = '' # Enter URL of the course page



# Enter code to initialize and set up telephony API client
# eg. client = ...
client = None



# Function to send an SMS
def send_sms(body):
    try:
        # Enter code from telephony API to send sms

        print("SMS sent.")
    except Exception as e:
        print(f"Error sending SMS: {e}")

# Initialize the webdriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)


def login():
    driver.get(login_url)

    # Enter username and password (fill in Xpaths)
    username_field = driver.find_element(By.XPATH, '')
    password_field = driver.find_element(By.XPATH, '')

    username_field.send_keys('')  # Enter your username
    password_field.send_keys('')  # Enter your password

    # Click the login button (fill in Xpath)
    login_button = driver.find_element(By.XPATH, '')
    login_button.click()

    # Wait for the next page to load after login
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '')) # Enter Xpath of element on next page
    )

    print("Logged in successfully.")

# Function to navigate to course page
def navigate_to_course_page():
    my_click("") # Enter Xpaths of all elements needed to navigate to course page
    my_click("") # Repeat as many times as necessary

    print("Navigated to the course page.")

# Function to click button
# Xpath = Xpath to button to press
def my_click(Xpath):

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, Xpath))
    )

    course_button = driver.find_element(By.XPATH, Xpath)
    course_button.click()


# Function to check course availability
# Argument is Xpath of course availability element
def check_course_availability(Xpath):

    # Find and click the button to reveal the course availability
    try:
        # OPTIONAL if after each refresh still need to navigate
        my_click("") # Enter Xpath of each element to be clicked
        my_click("") # Repeat as many times as necessary

        # Wait for the course availability to load
        # Xpath is path to course availability element
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            Xpath))
        )

        # Check the course availability
        course_availability = driver.find_element(By.XPATH,
                                                  Xpath)

        # replace 'available' with the text used to notify the course is now available
        if 'available' in course_availability.text.lower():  # Check for availability condition
            send_sms('The course is now available')  # Send an SMS notification
            print("Course is available.")
            return True  # Exit the loop if course is found
        else:
            print("Course not available yet.")
    except Exception as e:
        print(f"Error: {e}")
        return False


# Loop to keep checking for availability
login()
navigate_to_course_page()
while True:
    driver.refresh()
    if check_course_availability():
        break  # Stop checking once the course is available

    print(f"Course not available. Checking again...")
    time.sleep(30)  # Wait 30 seconds before checking again

# Quit the driver after checking
driver.quit()
