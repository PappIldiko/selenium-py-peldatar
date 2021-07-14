import time
from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/trickyelements.html"

browser = webdriver.Chrome(PATH)
try:
    browser.get(URL)

    elem_1 = browser.find_element_by_id("element1")
    elem_2 = browser.find_element_by_id("element2")
    elem_3 = browser.find_element_by_id("element3")
    elem_4 = browser.find_element_by_id("element4")
    elem_5 = browser.find_element_by_id("element5")

    res = browser.find_element_by_id("result")

    first_btn = browser.find_elements_by_xpath('//button')[0]
    # first_btn = browser.find_element_by_xpath('//button[@id="element2"]')
    first_btn.click()

    # print(first_btn.text)
    if res.text == f"{first_btn.text} was clicked":
        print(f"The '{first_btn.text} was clicked' text appeared correctly.")

except IndexError:
    time.sleep(2)
    print("There's no button present.")

finally:
    browser.quit()
