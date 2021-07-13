from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

PATH = "C:\\Windows\\chromedriver.exe"
URL = "https://www.idokep.hu/idojaras/Budapest"

browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    nemletezik_div = browser.find_element_by_id("nemletezik")
    # nemletezik_div = browser.find_element_by_id("hourlyForecastRow")
    # print(nemletezik_div.text())

except NoSuchElementException:
    print("Nem létezik 'nemletezik' id-jú elem.")

finally:
    browser.close()


# extra
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def check_element_by_id(id):
    try:
        browser.get(URL)
        browser.find_element_by_id(id)

    except NoSuchElementException:
        print(f"Nem létezik {id} id-jú elem.")

PATH = "C:\\Windows\\chromedriver.exe"
URL = "https://www.idokep.hu/idojaras/Budapest"
browser = webdriver.Chrome(PATH)

try:
    browser.get(URL)
    check_element_by_id("nemletezik")

except:
    print("Ez egy másik hiba.")

finally:
    browser.close()
