# -*- coding: utf-8 -*-

# =====================================================================
# write : moto
# latest update : 18.01.29
#
# usage : python vdate.py
#
# =====================================================================




import datetime, time

class VDATE:
    def getCurrentUnixTime(self):
        return time.time()

    def getToday(self):
        return datetime.date.today()

    def getFirstDayOfTheMonth(self):
        return datetime.date.today().replace(day=1)

    def getDateInterval(self):
        return datetime.date.today() - datetime.date.today().replace(day=1)




vdate = VDATE()

print vdate.getCurrentUnixTime()
print vdate.getToday()
print vdate.getFirstDayOfTheMonth()
print vdate.getDateInterval()
