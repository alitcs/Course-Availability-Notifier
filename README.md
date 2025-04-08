# Automatic Course Availability Checker

This Python script automatically checks for course availability on a specified webpage and sends an SMS notification when a spot becomes available. It's designed for programmers to easily adapt to their own use cases, such as registering for high-demand classes without constantly refreshing the page.

This script can also be extended to track product stock, event availability, or any webpage change.

---

## How It Works

1. Login: Script logs into your institution's course registration portal.  
2. Navigation: Navigates to the specific course listing page.  
3. Monitoring: Repeatedly refreshes the page and checks if the course becomes available.  
4. Notification: Sends a text message to your phone when the course is available.

---

## Setup Instructions

### 1. Prerequisites

- Python 3.6 or higher
- Google Chrome installed
- ChromeDriver installed (matching your Chrome version)
- Selenium: install with `pip install selenium`
- Twilio (or another SMS API): install with `pip install twilio`

### 2. Fill In the Blanks

Open the script and update the following sections:

#### Required Inputs

- `chrome_driver_path`: Path to your ChromeDriver executable
- `profile_path`: Path to your Chrome user data
- `profile_name`: Name of the Chrome profile to use
- `login_url`: The URL of your login page
- `account_sid`, `auth_token`, `from_number`, `to_number`: Your SMS provider's credentials (for example, from Twilio)

#### Login Info

In the `login()` function:
- Replace the empty XPaths for username, password fields, and login button
- Enter your login credentials

#### Navigation

In `navigate_to_course_page()`:
- Replace each `my_click("")` with actual XPaths to navigate to the course page

#### Availability Check

In `check_course_availability()`:
- Replace the XPaths to reveal and read course availability
- Replace `'available'` with the keyword used by your system to indicate open spots

---

## SMS Notification

Make sure to initialize your telephony client (e.g., Twilio):

```python
client = Client(account_sid, auth_token)
```

And complete the `send_sms()` function:

```python
client.messages.create(
    body=body,
    from_=from_number,
    to=to_number
)
```

---

## Loop Behavior

The script will:
- Refresh the course page every 30 seconds (adjustable via `time.sleep()`)
- Exit automatically after sending an SMS when availability is detected

---

## Example Use Cases

- University Registration: Monitor limited enrollment courses
- Product Restocks: Alert when an item is back in stock
- Concert/Event Ticket Drops: Be the first to grab a seat
- Job or Application Portals: Know when a new posting appears

---

## Notes

- This script uses your existing Chrome profile to maintain login sessions (cookies, multi-factor authentication, etc.)
- Ensure your XPath selections are stable and accurate
- Use responsibly; too frequent requests may violate the terms of service of the target site

---

## Contributions

Feel free to fork, improve, or extend this tool for your specific needs. Pull requests and issue submissions are welcome.

---

## License

MIT License – free for personal and commercial use.
