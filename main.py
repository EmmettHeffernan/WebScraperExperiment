import os
import time
import requests
import shutil # to save it locally
from selenium import webdriver

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "bin/chromedriver_for_mac")
print(DRIVER_BIN)

driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F")

username = driver.find_element_by_name("username")
username.clear()
username.send_keys("genrefluid98")
password = driver.find_element_by_name("password")
password.clear()
password.send_keys("3H3ffmcd3rp")

login_button = driver.find_element_by_xpath("/html/body/div/div/div/div/form/div/fieldset/button")
login_button.click()
time.sleep(5)
dropdown = driver.find_element_by_id("USER_DROPDOWN_ID")
dropdown.click()
profile = driver.find_element_by_class_name("_1YWXCINvcuU7nk0ED-bta8")
profile.click()
time.sleep(3)
saved = driver.find_element_by_xpath('//a[@href="'+"/user/GenreFluid98/saved/"+'"]')
saved.click()
time.sleep(3)
post_links = driver.find_elements_by_tag_name('a')
for links in post_links:
    if str(links.get_attribute('class')) == 'SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE':
        driver.get(links.get_attribute('href'))
        images = driver.find_elements_by_tag_name('img')



# for image in images:
#     print(str(image.get_attribute('alt')).lower())
#
#     # if search(("post image"), str(image.get_attribute('alt')).lower()):
#         # print("Found!")
#         # img_list.append(image.get_attribute('src'))
#     # else:
#     #     print(str(image.get_attribute('alt')))
#
# print(img_list)

# for items in posts:
#
#     expand = posts.find_element_by_class_name("_35zWJjb5RJMIMkexZ2Prus RvLtAcdRtbOQbhFB7MD_T")
#     expand.click()
# /html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/a/
