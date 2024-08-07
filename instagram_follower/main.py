from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
import time
import os

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

URL = "https://www.instagram.com/accounts/login/"
EMAIL = os.environ['EMAIL']
PASSWORD = os.environ["PASSWORD"]


def follow():
    follow_buttons = driver.find_elements(By.XPATH, "/html/body/div[6]/div[2]/div/div/div[1]/div/div["
                                                    "2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div["
                                                    "1]/div/div/div/div[3]/div/button")
    for button in follow_buttons:
        try:
            time.sleep(2)
            button.click()
        except ElementClickInterceptedException:
            cancel_button = driver.find_element(By.XPATH, "/html/body/div[7]/div[1]/div/div["
                                                          "2]/div/div/div/div/div/div/button[2]")
            cancel_button.click()


def find_followers():
    popup_window = driver.find_element(By.XPATH,
                                       "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div["
                                       "2]/div/div/div[3]")

    for i in range(5):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].scrollHeight;",
                              popup_window)
        time.sleep(2)


driver = webdriver.Chrome(options=options)

driver.get(URL)

time.sleep(5)

username = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div["
                                         "1]/div[2]/form/div/div[1]/div/label/input")
username.send_keys(EMAIL, Keys.TAB)

password = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
password.send_keys(PASSWORD, Keys.TAB)

driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button").click()

time.sleep(10)

driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div["
                              "2]/section/main/div/div/div/div/div").click()

time.sleep(10)

driver.find_element(By.XPATH,
                    "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()

print("successfully logged in")

print("switching to linux memes profile")
driver.get("https://www.instagram.com/linux_memes/")

# //*[@id="mount_0_0_81"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button
# driver.find_element(By.XPATH, "//button[contains(text(), 'Follow')]").click()
# print("following linux_memes")

time.sleep(10)

all_followers = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div["
                                              "2]/section/main/div/header/section[3]/ul/li[2]/div/a")
all_followers.click()

print("clicked linux_memes followers")

time.sleep(10)

find_followers()

follow()


# main_window = driver.current_window_handle
# for handle in main_window:
#     if handle != main_window:
#         popup = handle
#     else:
#         print(main_window)
#
# follow_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Follow')]")

# get followers window


# driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div")

# get number of followers all_followers = driver.find_element(By.XPATH, "//*[@id='mount_0_0_kI']/div/div/div[
# 2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/div/a/span/span").text

# print(f"{all_followers.text} : {type(all_followers.text)}")

# for button in follow_buttons:
#

# driver.quit()


# /html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[
# 1]/div/div/div /html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[
# 1]/div/div[1]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span //*[@id="mount_0_0_Ui"]/div/div/div[
# 2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[3]/ul/li[2]/div/a print(main_window) //*[
# @id='mount_0_0_y7']/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div login_button =
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='loginForm']/div/div[3]/button")))
# username = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
# "//*[@id='loginForm']/div/div[1]/div/label/input"))) password = WebDriverWait(driver, 10).until(
# EC.visibility_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input"))) //*[
# @id='loginForm']/div/div[1]/div/label/input /html/body/div[2]/div/div/div[2]/div/div/div[
# 1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input
