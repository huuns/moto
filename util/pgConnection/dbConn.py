# =====================================================================
# write : moto
# latest update : 16.03.15.
#
# dependency : psycopg2==2.6.1 (https://pypi.python.org/pypi/psycopg2)
# 
# usage : object create 
# =====================================================================

import psycopg2

class pg_DB_Management:
  conn, cur = None, None

  def connect(self):
    try:
      self.conn = psycopg2.connect("dbname='test_db' user='postgres' host='localhost' password='bidksijfks139g3'")
    except:
      print "not connect"
    self.cur = self.conn.cursor()

  def disconnect(self):
    self.cur.close()
    self.conn.close()
