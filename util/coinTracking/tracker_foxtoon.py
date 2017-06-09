# -*- coding: utf-8 -*-

# =====================================================================
# write : moto
# latest update : 17.05.24.
#
# parsing --> db --> csv --> s3
# viewing --> s3
#
# =====================================================================

import datetime, sys, sqlite3, json, time, re
from robobrowser import RoboBrowser
from dbconn import DBCONN
from os import popen

reload(sys)
sys.setdefaultencoding('utf-8')


class TRACKER_FOXTOON:

    dbconn = DBCONN()
    dbconn.connect()

    todayString = str(datetime.date.today())

    coinTopElements = None

    product_title_list, product_price_list = None, None

    def getData(self):

        # temp
        sqlString = "DELETE FROM coin_foxtoon WHERE date='%s'" % (self.todayString)
        self.dbconn.cur.execute(sqlString, )
        # temp

        browser = RoboBrowser(history=True,
            user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/33.0.1750.152 Chrome/33.0.1750.152 Safari/537.36')

        # foxtoon login ---------------------------------------------------------------- start
        browser.open('http://www.foxtoon.com/login')
        form = browser.get_form(id='login-form')
        form['email'].value = 'email value'
        form['pw'].value = 'password value'
        browser.submit_form(form)
        # foxtoon login ---------------------------------------------------------------- end

        url_content = 'http://www.foxtoon.com/purchase'
        browser.open(url_content)
        self.coinTopElements = browser.find_all('li', class_='goods')

        self.product_title_list, self.product_price_list = [], []

        for idx, cel in enumerate(self.coinTopElements):

            for pt in cel.find_all('span', class_='content'):
                print pt.get_text()
                self.product_title_list.append(pt.get_text())

            for pp in cel.find_all('span', class_='price'):
                print pp.get_text()
                self.product_price_list.append(pp.get_text())

    def updateTable(self):

        sqlString = "SELECT Count(*) FROM coin_foxtoon WHERE date='%s'" % (self.todayString)
        self.dbconn.cur.execute(sqlString, )
        rows = self.dbconn.cur.fetchall()

        if rows[0][0] == 0:
            for idx, pt in enumerate(self.product_title_list):
                coinpack_name = pt.split(' ')[0]
                coinpack_count = sum(map(int, re.findall('\d+', pt)))
                coinpack_price = int(self.product_price_list[idx][:-1].replace(',',''))

                sqlString = "INSERT INTO coin_foxtoon (date, coinpack_name, coinpack_count, coinpack_price, onecoin_price) VALUES('%s', '%s', %d, %d, %f)" % (self.todayString, coinpack_name, coinpack_count, coinpack_price, float(coinpack_price)/coinpack_count)
                print sqlString

                # SQL 쿼리 실행
                self.dbconn.cur.execute(sqlString, )
                self.dbconn.conn.commit()
        else:
            print "exist foxtoon today information"


    def jsonCreate2s3(self):

        output = {}

        sqlString = "SELECT DISTINCT coinpack_name FROM coin_foxtoon"
        self.dbconn.cur.execute(sqlString, )
        coninpack_names = self.dbconn.cur.fetchall()

        for name in coninpack_names:

            sqlString = "SELECT coinpack_price FROM coin_foxtoon WHERE coinpack_name='%s'" % (name[0])
            self.dbconn.cur.execute(sqlString, )
            coninpack_prices = self.dbconn.cur.fetchall()

            coninpack_prices = [x[0] for x in coninpack_prices]
            print coninpack_prices

            output[name[0]] = coninpack_prices


        with open ('./json/foxtoon_coin.json', 'w') as f:
            f.write("{\n")
            for idx, key in enumerate(output.keys()):
                if idx == 0:
                    f.write('"%s": %s' %( key, output[key] ) )
                else:
                    f.write(',\n"%s": %s' %( key, output[key] ) )
            f.write("\n}")

        popen('aws s3 sync ./json     s3://!!!!!!!!!  --acl public-read --delete --cache-control max-age=3600')


    def onecoin_price_jsonCreate2s3(self):
        output = {}

        sqlString = "SELECT DISTINCT coinpack_name FROM coin_foxtoon"
        self.dbconn.cur.execute(sqlString, )
        coninpack_names = self.dbconn.cur.fetchall()

        for name in coninpack_names:

            sqlString = "SELECT onecoin_price FROM coin_foxtoon WHERE coinpack_name='%s' AND date='%s'  " % (name[0], self.todayString)
            self.dbconn.cur.execute(sqlString, )
            onecoin_prices = self.dbconn.cur.fetchall()

            onecoin_prices = [x[0] for x in onecoin_prices]
            print onecoin_prices

            output[name[0]] = onecoin_prices

        with open ('./json/foxtoon_onecoin.json', 'w') as f:
            f.write("{\n")
            for idx, key in enumerate(output.keys()):
                if idx == 0:
                    f.write('"%s": %s' %( key, output[key] ) )
                else:
                    f.write(',\n"%s": %s' %( key, output[key] ) )
            f.write("\n}")

        self.dbconn.disconnect()

        popen('aws s3 sync ./json     s3://://!!!!!!!!!  --acl public-read --delete --cache-control max-age=3600')
