import time
import pywhatkit
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#Take the current time on your desktop
date = datetime.datetime.now()
hour = date.hour
minute = date.minute + 1

message = input("Enter the message: ")

phone_number = input("Enter the number: ")

# Send the message in a feel seconds
#pywhatkit.sendwhatmsg(phone_number, message, hour, minute)

# Send the message instantly
pywhatkit.sendwhatmsg_instantly(phone_number, message)

time.sleep(7)

# webdriver setup
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.switch_to.window(driver.window_handles[0])

# Find the enter button on whataspp web and click it
send_button = driver.find_element(By.XPATH, '//button[@data-testid="compose-btn-send"]')
send_button.click()

