import pyautogui
import webbrowser
import time

# Define the image filenames of the elements you need to interact with
options_image = "options.png"  # Image of an unread email
mark_as_read_button_image = "mark_as_read.png"  # Image of the 'Mark as Read' button

webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
time.sleep(2)

# Locate the unread email
# options_location = pyautogui.locateCenterOnScreen(options_image, confidence=0.8)
# pyautogui.click(options_location)  # Click the unread email
pyautogui.moveTo(470, 220)
pyautogui.click()
time.sleep(2)  # Wait for the email to open

while True:
    try:
        mark_as_read_location = pyautogui.locateCenterOnScreen(
            mark_as_read_button_image, confidence=0.7
        )

        pyautogui.click(mark_as_read_location)  # Click the unread email
        time.sleep(2)  # Wait for the email to open
        break
    except:
        print("didn't find mark_as_read image")  # Close the email (if needed)

pyautogui.hotkey("ctrl", "w")  # Close the email window
time.sleep(1)  # Wait for the email to close
