from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"
URL = "http://localhost:9999/todo.html"

browser = webdriver.Chrome(PATH)

try:
    browser.maximize_window()
    browser.get(URL)

    active_todos = browser.find_elements_by_xpath('//span[@class="done-false"]')
    for i in active_todos:
        print(i.text)

except:
    print("Sg went wrong.")

finally:
    browser.quit()
