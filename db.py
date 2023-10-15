import psycopg2
from parser import get_riggles

class server():

    def __init__(self, db_name='postgres', db_user='postgres', db_password='1234',\
                      db_host='172.17.0.1', db_port='5432'):

        self.db_name=db_name
        self.db_user=db_user
        self.db_password=db_password
        self.db_host=db_host
        self.db_port = db_port


    def create_connection(self):
        """ Create connection to existing database """

        connection=None

        try:
            connection = psycopg2.connect(
                database=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port=self.db_port
            )

        except ConnectionError as e:
            return 'Check your verification data'

        return connection


    def create_table(self, name='riggles'):
        """ Add new table into database """

        with self.create_connection() as conn:
            curs = conn.cursor()

            curs.execute(f"CREATE TABLE IF NOT EXISTS {name}\
            	(id int, \
            	riggle text, \
            	answer text, \
            	created text)")




    def add_riggle(self, for_insert:list) -> int:
        """" Method get data about riggle and return a number of elemnts that exists in table already """

        exist = 0

        with self.create_connection() as conn:
            curs = conn.cursor()

            curs.execute('SELECT DISTINCT(id) FROM riggles;')
            ids = curs.fetchall()

            for i in for_insert:
                id = i['id']
                riggle = i['question']
                answer = i['answer']
                create = i['created_at'].split('T')[0]

                if id not in ids:
                    curs.execute("INSERT INTO riggles (id, riggle, answer, created) VALUES (%s, %s, %s, %s)",\
                    (id, riggle, answer, create))

                else:
                    exist += 1

            if exist>0:
                for_insert = get_riggles(n=exist)
                return self.add_riggle(for_insert)

            else:
                return None