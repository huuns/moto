# =====================================================================
# write      : moto
# update     : 2016.10.19.
# dependency : psycopg2==2.6.1 (https://pypi.python.org/pypi/psycopg2)
# =====================================================================

import psycopg2

class T1_DB_Management:
  conn, cur = None, None

  def connect(self):
    try:
      self.conn = psycopg2.connect("dbname='t1' user='postgres' host='localhost' password='iblblbifgilfidisksiwkirfkfidksiif90180fg08cdk1lkf98vcjkc01'")
    except:
      print "not connect"
    self.cur = self.conn.cursor()

  def disconnect(self):
    self.cur.close()
    self.conn.close()


class T2_DB_Management:
  conn, cur = None, None

  def connect(self):
    try:
      self.conn = psycopg2.connect("dbname='t2' user='postgres' host='localhost' password='059fv09sdu0f9u23lksdjlkfjs0q9238uas089ufskjlcsnsoiw239083uf'")
    except:
      print "not connect"
    self.cur = self.conn.cursor()

  def disconnect(self):
    self.cur.close()
    self.conn.close()

# =====================================================================
