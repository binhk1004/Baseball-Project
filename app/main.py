import bs4
from selenium import webdriver
from selenium.webdriver.support.select import Select


class BaseballCrawler():
    def __init__(self, url):
        driver = webdriver.Chrome('/Users/binhk1004/Downloads/chromedriver')
        url = driver.get('https://www.koreabaseball.com/Default.aspx?vote=true')
        self.__move_page()


    def __move_page(self):
        soup = bs4.BeautifulSoup(url, 'html.parser')
        test = soup.find('body')
        print(test)













if __name__ == '__main__':
    BaseballCrawler()