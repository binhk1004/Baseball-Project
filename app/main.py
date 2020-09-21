from bs4 import BeautifulSoup
from selenium import webdriver
from Database.model import HandlingDatabase

driver = webdriver.Chrome('/Users/binhk1004/Downloads/chromedriver')
url = driver.get('https://www.koreabaseball.com/Default.aspx?vote=true')

class baseball_crawler():
    def __init__(self):
        self.__move_page()
        HandlingDatabase()


    def __move_page(self):
        record_page = driver.find_element_by_xpath('//*[@id="lnb"]/li[3]')
        record_page.click()
        driver.switch_to.window(driver.window_handles[-1])
        result = driver.current_url
        self.__record_crawler(result)

    def __record_crawler(self, result):
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        self._batting_average_crawler(soup)
        # self.__homerun_crawler(soup)
        # self.__average_ERA_crawler(soup)
        # self.__vitory_pitcher_crawler(soup)

    def _batting_average_crawler(self, soup):
        averages = soup.select('ol.rankList')[0].select('li')
        for average in averages:
            batting_average_data = {
            'player_name':average.text.split()[0],
            'team_name':average.text.split()[1],
            'batting_average':average.text.split()[2]
            }
            return HandlingDatabase()



    def __homerun_crawler(self, soup):
        homerun_top5 = soup.select('div.player_top5 > ol.rankList')[1].text
        print(homerun_top5)

    def __average_ERA_crawler(self, soup):
        average_ERA_top5 = soup.select('div.record_list.mt40.mb30 > div.record.mr15')[0].text
        print(average_ERA_top5)

    def __vitory_pitcher_crawler(self, soup):
        vitory_pitcher_top5 = soup.select('div.record_list.mt40.mb30 > div.record')[1].text
        print(vitory_pitcher_top5)











if __name__ == '__main__':
    baseball_crawler()