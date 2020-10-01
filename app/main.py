import pymysql
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('/Users/hyun/Downloads/chromedriver')
url = driver.get('https://www.koreabaseball.com/Default.aspx?vote=true')

class BaseballCrawler():
    def __init__(self):
        self.__move_page()
        self.__connet_database()


    def __move_page(self):
        record_page = driver.find_element_by_xpath('//*[@id="lnb"]/li[3]')
        record_page.click()
        driver.switch_to.window(driver.window_handles[-1])
        result = driver.current_url
        self.__record_crawler(result)

    def __record_crawler(self, result):
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        self.__batting_average_crawler(soup)
        # self.__homerun_crawler(soup)
        # self.__average_ERA_crawler(soup)
        # self.__vitory_pitcher_crawler(soup)

    def __batting_average_crawler(self, soup):
        baseball_db = self.__connet_database()
        averages = soup.select('ol.rankList')[0].select('li')
        for average in averages:
            batting_average_data = [
            average.text.split()[0],
            average.text.split()[1],
            average.text.split()[2]
            ]
            self.__insert_data(baseball_db, batting_average_data)

    def __homerun_crawler(self, soup):
        homerun_top5 = soup.select('div.player_top5 > ol.rankList')[1].text
        print(homerun_top5)

    def __average_ERA_crawler(self, soup):
        average_ERA_top5 = soup.select('div.record_list.mt40.mb30 > div.record.mr15')[0].text
        print(average_ERA_top5)

    def __vitory_pitcher_crawler(self, soup):
        vitory_pitcher_top5 = soup.select('div.record_list.mt40.mb30 > div.record')[1].text
        print(vitory_pitcher_top5)

    def __connet_database(self):
        baseball_db = pymysql.connect(
            user='root',
            password='qlsgus4613',
            host='127.0.0.1',
            db='Baseball_Record',
            charset='utf8'
        )
        self.__create_table(baseball_db)
        return baseball_db

    def __create_table(self, baseball_db):

        sql = '''CREATE TABLE batting_average_top5 (
        id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
        player_name varchar(255),
        team_name varchar(255),
        batting_average varchar(255)
        )
        '''

        cur = baseball_db.cursor()
        cur.execute(sql)


    def __insert_data(self, baseball_db, batting_average_data):
        cur = baseball_db.cursor()
        sql = '''INSERT INTO batting_average_top5 (player_name, team_name, batting_average) values (batting_average_data)'''
        print(batting_average_data[0])
        print(batting_average_data[1])
        print(batting_average_data[2])

        cur.execute(sql)

        baseball_db.commit()
        baseball_db.close()





if __name__ == '__main__':
    BaseballCrawler()