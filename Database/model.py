import pymysql

class handling_database():
    def __init__(self):
        self.__connet_database()


    def __connet_database(self):
        baseball_db = pymysql.connect(
            user='root',
            password='qlsgus4613',
            host='127.0.0.1',
            db='Baseball_Record',
            charset='utf8'
        )
        return self.__create_table(baseball_db)

    def __create_table(self,baseball_db):
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
        return baseball_db

    def _insert_data(self, baseball_db, batting_average_data):
        sql = '''INSERT INTO batting_average_top5 (player_name, team_name, batting_average) values(%s, %s, %s)'''

        cursor = baseball_db.cursor()
        cursor.execute(sql,batting_average_data)

        baseball_db.commit()
        baseball_db.close()