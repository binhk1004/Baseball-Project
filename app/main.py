from time import sleep

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.select import Select

class BaseballCrawler():
    def __init__(self):
        self.__move_page()


    def __move_page(self):
        driver = webdriver.Chrome('/Users/binhk1004/Downloads/chromedriver')
        url = driver.get('https://www.koreabaseball.com/Default.aspx?vote=true')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        test = driver.find_element_by_xpath('//*[@id="lnb"]/li[3]')
        test.click()
        sleep(3)















if __name__ == '__main__':
    BaseballCrawler()