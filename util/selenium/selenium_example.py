

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome('/Users/moto/dev_moto/util/selenium/chromedriver', chrome_options=chrome_options)
driver.get("http://ngee.tistory.com")
