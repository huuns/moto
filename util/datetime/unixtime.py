# -*- coding: utf-8 -*-

# =====================================================================
# write : moto
# latest update : 18.01.27
#
# usage : python unixtime.py
#
# =====================================================================




import datetime, time

class UNIXTIME:
    def getCurrentUnixTime(self):
        return time.time()

    def getTodayUnixTime(self):
        return int(datetime.date.today().strftime("%s")) * 1000

    def getNextWeekUnixTime(self):
        return int((datetime.date.today() + datetime.timedelta(days=7)).strftime("%s")) * 1000

    def getLastWeekUnixTime(self):
        return int((datetime.date.today() - datetime.timedelta(days=7)).strftime("%s")) * 1000




unixtime = UNIXTIME()

print unixtime.getCurrentUnixTime()
print unixtime.getTodayUnixTime()
print unixtime.getNextWeekUnixTime()
print unixtime.getLastWeekUnixTime()

 
