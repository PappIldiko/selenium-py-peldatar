import csv
from selenium import webdriver
import time

browser = webdriver.Chrome("C:\\Windows\\chromedriver.exe")

try:
    browser.maximize_window()
    browser.get("http://localhost:9999/another_form.html")


    def find_and_clear_by_id(id):
        element = browser.find_element_by_id(id)
        element.clear()
        return element


    submit_btn = browser.find_element_by_id("submit")

    with open('table_in.csv', 'r', encoding="utf-8") as csvf:
        csvreader = csv.reader(csvf, delimiter=',')
        next(csvreader)
        for row in csvreader:
            print(row)
            find_and_clear_by_id("fullname").send_keys(row[0])
            find_and_clear_by_id("email").send_keys(row[1])
            find_and_clear_by_id("dob").send_keys(row[2])
            find_and_clear_by_id("phone").send_keys(row[3])
            submit_btn.click()

    time.sleep(2.0)
    export_table_to_csv = browser.find_element_by_xpath('//button[text()="Export HTML table to CSV file"]')
    export_table_to_csv.click()
    time.sleep(2.0)

except:
    print("Sg went wrong.")

finally:
    browser.quit()
