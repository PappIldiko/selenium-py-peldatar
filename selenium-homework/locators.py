import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/kitchensink.html"

browser = webdriver.Chrome(PATH)

browser.maximize_window()
browser.get(URL)

try:
    # 1
    # elem_by_id = browser.find_element_by_id("mousehover")
    # assert elem_by_id.text == "Mouse Hover"
    # print(elem_by_id.text)

    # 2
    # back_btn = browser.find_element_by_xpath('//a[@href="index.html"]')
    # back_btn.click()
    #
    # index_page = browser.find_element_by_xpath('//h1[text()="Selenium Practice Pages"]')
    # if index_page.text == "Selenium Practice Pages":
    #     print("Back button is working.")
    #

    # 3
    # honda_radio_btn = browser.find_element_by_id('hondaradio')
    # honda_radio_btn.click()
    #
    # bmw_parent = browser.find_element_by_xpath('//input[@id="bmwradio"]/../../legend')
    # print(bmw_parent.text)
    # assert bmw_parent.text == "Radio Button Example"

    # 4
    # select_dropdown = browser.find_element_by_xpath('//select[@id="carselect"]/option[@value="honda"]')
    # select_dropdown.click()

    # 4/b - Kocka - by id dropdown menüben
    # select_dropdown = browser.find_element_by_id("carselect")
    # my_cars = Select(select_dropdown)
    # for i in my_cars.options:
    #     print(i.text)

    # 5
    # def checkbox_pusher(route):
    #     checkbox = browser.find_element_by_xpath(route)
    #     checkbox.click()
    #
    # checkbox_pusher('//fieldset/label[@for="bmw"]/input[@type="checkbox"]')
    # checkbox_pusher('//fieldset/label[@for="honda"]/input[@type="checkbox"]')
    # checkbox_pusher('//fieldset/label[@for="benz"]/input[@type="checkbox"]')

    # 6
    # open_window = browser.find_element_by_id('openwindow')
    # print(open_window.tag_name)
    # open_window.click()
    # print(browser.title)

    # 7
    # enter_name_field = browser.find_element_by_xpath('//input[@name="enter-name"]')
    # enter_name_field.send_keys('valami')
    # confirm_btn = browser.find_element_by_id("confirmbtn")
    # confirm_btn.click()
    # alert!!!

    # 8 Emese - following sibling
    # teso_kereses = browser.find_element_by_xpath("//legend[contains(text(), 'Switch to Window Example' )]/following-sibling::button")
    # print(teso_kereses.text)

    # 9 Kocka
    # elem_by_id = browser.find_element_by_id('hide-textbox').get_attribute("type")
    # print(elem_by_id)

    # 10 Kocka
    table = browser.find_element_by_name("courses")
    print(table.text)


except:
    time.sleep(2)
    print("Sg went wrong.")

finally:
    browser.quit()
