import pymysql
class DbOperation:
    def __init__(self,host,user,password,database,port,charset):
        self.host = host
        self.user =user
        self.password = password
        self.database =database
        self.port =port
        self.charset = charset

    def get_conn(self):
        try:
            conn = pymysql.Connection(host=self.host,user=self.user,password=self.password,database=self.database,port=self.port,charset=self.charset)
            return conn
        except Exception as e:
            print(e,'connect failed')


    def search_data(self,sql):
        try:
            conn = self.get_conn()
            cur = conn.cursor()
            cur.execute(sql)
            res = cur.fetchall()
        except Exception as e:
            print(e,'cur exec error')
            conn.rollback()
        finally:
            cur.close()
            conn.close()
        return res

    def update_data(self,sql):
        try:
            conn = self.get_conn()
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
        except Exception as e:
            conn.rollback()
        finally:
            cur.close()
            conn.close()

