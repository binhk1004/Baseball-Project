from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('/Users/hyun/Downloads/chromedriver 2')
url = driver.get('https://www.koreabaseball.com/Default.aspx')

record_page = driver.find_element_by_xpath('//*[@id="lnb"]/li[3]')
record_page.click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

averages = soup.select('ol.rankList')[0].select('li')
homeruns = soup.select('ol.rankList')[1].select('li')

def remove_list(averages, homerun):
    for data in (averages, homerun):
        baseball_crawler(data)

def baseball_crawler(data):
    for item in data:
        print(item.text)

remove_list(averages, homeruns)

