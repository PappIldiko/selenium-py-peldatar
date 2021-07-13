from selenium import webdriver

PATH = "C:\\Windows\\chromedriver.exe"
URL = "https://www.idokep.hu/idojaras/Budapest"

browser = webdriver.Chrome(PATH)
browser.get(URL)

browser.close()

