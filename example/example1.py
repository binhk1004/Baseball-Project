from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('/Users/binhk1004/Downloads/chromedriver')
url = driver.get('https://www.koreabaseball.com/Default.aspx')

record_page = driver.find_element_by_xpath('//*[@id="lnb"]/li[3]')
record_page.click()