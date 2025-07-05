from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = "https://www.google.co.kr/lmghp"
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=10)
