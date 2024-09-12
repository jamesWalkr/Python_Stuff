from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

ZILLOW_URL = "https://appbrewery.github.io/Zillow-Clone/"
GOOGLE_FORM = "https://forms.gle/oTkpKRXLsBSLjzGW8"

reuqest = requests.get(ZILLOW_URL)

web_page = reuqest.text

soup = BeautifulSoup(web_page, "html.parser")

property_links = soup.select(".StyledPropertyCardDataArea-anchor")
property_prices = soup.select(".PropertyCardWrapper__StyledPriceLine")
property_addresses = soup.select("address")

list_of_property_links = [link.get("href") for link in property_links]
list_of_property_prices = [price.text for price in property_prices]
list_of_property_addresses = [
    " ".join(address.text.strip().replace("|", "").split())
    for address in property_addresses
]


# for link in property_links:
#    list_of_property_links.append(link.get("href"))

# print(len(list_of_property_links))
# print(len(list_of_property_prices))
# print(list_of_property_addresses)


# Get google form
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get(GOOGLE_FORM)

time.sleep(5)


for i in range(len(list_of_property_prices)):

    # enter 1st element fomr each of the lists
    property_input = driver.find_element(
        By.XPATH,
        "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )
    property_input.send_keys(list_of_property_addresses[i], Keys.TAB)
    # print("answered 1st question")

    price_input = driver.find_element(
        By.XPATH,
        "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )
    price_input.send_keys(list_of_property_prices[i], Keys.TAB)
    # print("answered 2nd question")

    property_link_input = driver.find_element(
        By.XPATH,
        "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )
    property_link_input.send_keys(list_of_property_links[i], Keys.TAB)
    # print("answered 3rd question")

    submit_button = driver.find_element(
        By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div"
    ).click()
    # print("survey submitted")

    submit_another_response = driver.find_element(
        By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a"
    ).click()

    time.sleep(5)

driver.quit()

# print(soup)
