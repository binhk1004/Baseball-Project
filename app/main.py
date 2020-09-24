import pymysql
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('/Users/binhk1004/Downloads/chromedriver')
url = driver.get('https://www.koreabaseball.com/Default.aspx?vote=true')

class BaseballCrawler():
    def __init__(self):
        self.__move_page()
        HandlingDataBase()


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
        baseball_db = HandlingDataBase().connet_database()
        for average in averages:
            batting_average_data = {
            'player_name':average.text.split()[0],
            'team_name':average.text.split()[1],
            'batting_average':average.text.split()[2]
            }
            print(batting_average_data)
            HandlingDataBase().insert_data(baseball_db, batting_average_data)



    def __homerun_crawler(self, soup):
        homerun_top5 = soup.select('div.player_top5 > ol.rankList')[1].text
        print(homerun_top5)

    def __average_ERA_crawler(self, soup):
        average_ERA_top5 = soup.select('div.record_list.mt40.mb30 > div.record.mr15')[0].text
        print(average_ERA_top5)

    def __vitory_pitcher_crawler(self, soup):
        vitory_pitcher_top5 = soup.select('div.record_list.mt40.mb30 > div.record')[1].text
        print(vitory_pitcher_top5)


class HandlingDataBase():
    def __init__(self):
        self.connet_database()

    def connet_database(self):
        baseball_db = pymysql.connect(
            user='root',
            password='qlsgus4613',
            host='127.0.0.1',
            db='Baseball_Record',
            charset='utf8'
        )

    def __create_table(self, baseball_db):

        sql = '''CREATE TABLE batting_average_top5 (
        id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
        player_name varchar(255),
        team_name varchar(255),
        batting_average varchar(255)
        )
        '''

        cursor = baseball_db.cursor()
        cursor.execute(sql)
        baseball_db.commit()

    def insert_data(self, baseball_db, batting_average_data):

        for data in batting_average_data:

            sql = '''INSERT INTO batting_average_top5 (player_name, team_name, batting_average) values (data)'''


            cursor = baseball_db.cursor()
            cursor.execute(sql, data)

        baseball_db.commit()
        baseball_db.close()





if __name__ == '__main__':
    BaseballCrawler()