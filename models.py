
import urllib.parse as urlparse
import psycopg2
import os
import json
import datetime
import routes


class DataModel:
    
    def connect_to_database(self):
        try:
            conn = ""
            out = []
            url = urlparse.urlparse(os.environ['DATABASE_URL'])
            dbname = url.path[1:]
            user = url.username
            password = url.password
            host = url.hostname
            port = url.port
            conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
            return conn.cursor()
        except Exception as e:
            out = {'err' : str(e)}
            return json.dumps(out)

    def insert_into_database(self,text,type):
        try:
            cur = connect_to_database()
            cur.execute("""INSERT INTO thought VALUES(text,datetime.now(),type,0,)""")    
        except:
            '%s text not inserted', text

    def get_thoughts(self):
        try:
            cur = self.connect_to_database()
            cur.execute("""SELECT * from person""")
            out = cur.fetchall()
            for row in out:
                print('Printing rows')
                print(row)
        except Exception as e:
            out = {"err": str(e)}
        return json.dumps(out)



