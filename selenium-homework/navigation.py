# egyelőre nem fut le
import time

from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/general.html"

browser = webdriver.Chrome(PATH)

# try:
browser.maximize_window()
browser.get(URL)

# def link_visit(url, ):


active_links = browser.find_elements_by_xpath('//a')
href_links = []
for i in active_links:
    print(i.get_attribute("href"))
    href_links.append(i)
for i in href_links:
    i.click()
    time.sleep(1.0)
    # if a.href == új url: - az új url-t még nem tudom
    browser.back()

# except:
#     print("Sg went wrong.")
#
# finally:
#     browser.quit()
