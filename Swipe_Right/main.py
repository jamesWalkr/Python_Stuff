from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

# from selenium.webdriver.support.relative_locator import locate_with

import time

EMAIL = ""
PASSWORD = ""

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://tinder.com")

time.sleep(20)

sign_in = driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a",
).click()

print("sign in button clicked")

time.sleep(15)

main_window = driver.current_window_handle

facebook_login = driver.find_element(
    By.XPATH,
    "//*[@id='u1146625330']/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button",
).click()

print("Facebook login clicked")

time.sleep(15)

for handle in driver.window_handles:
    if handle != main_window:
        popup = handle
        driver.switch_to.window(popup)

print(driver.title)

email = driver.find_element(By.XPATH, "//*[@id='email']")
email.send_keys(EMAIL, Keys.TAB)

password = driver.find_element(By.NAME, "pass")
password.send_keys(PASSWORD, Keys.TAB)

facebook_login_button = driver.find_element(By.NAME, "login")
facebook_login_button.send_keys(Keys.ENTER)

time.sleep(30)

print(driver.title)

continue_as_me = driver.find_element(
    By.XPATH, ("//span[text()='Continue as James']")
).click()

time.sleep(10)

driver.switch_to.window(main_window)

print("switiching to the main window")

accept_cookies = driver.find_element(
    By.XPATH, "//*[@id='u1146625330']/div/div[2]/div/div/div[1]/div[1]/button"
).click()

print("cookies accepted.")

time.sleep(5)

allow_location_tracking = driver.find_element(
    By.XPATH, "//*[@id='u1146625330']/div/div[1]/div/div/div[3]/button[1]"
).click()

print("location tracking allowed.")

time.sleep(5)

deny_notifications = driver.find_element(
    By.XPATH, "//*[@id='u1146625330']/div/div/div/div/div[3]/button[2]"
).click()

print("app notifications denied.")

time.sleep(5)

maybe_later = driver.find_element(
    By.XPATH, "//*[@id='u1146625330']/div/div/div/div[3]/button[2]"
).click()

print("see likes later clicked")

time.sleep(15)

for x in range(5):
    like_button = driver.find_element(
        By.XPATH,
        "//*[@id='u-1419960890']/div/div[1]/div[2]/div/main/div/div[1]/div[2]/div/div/div[3]/div/div/div/button",
    )
    like_button.click()
    print("like button clicked")
    time.sleep(10)

print("Done.")
# driver.quit()
