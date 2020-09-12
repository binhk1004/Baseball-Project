from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('/Users/binhk1004/Downloads/chromedriver')
url = driver.get('https://www.koreabaseball.com/Default.aspx?vote=true')

class BaseballCrawler():
    def __init__(self):
        self.__move_page()


    def __move_page(self):
        record_page = driver.find_element_by_xpath('//*[@id="lnb"]/li[3]')
        record_page.click()
        driver.switch_to.window(driver.window_handles[-1])
        result = driver.current_url
        self.__record_crawler(result)

    def __record_crawler(self, result):
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        test = soup.find('body > div.record_list')
        print(test)






if __name__ == '__main__':
    BaseballCrawler()