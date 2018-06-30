






import datetime, time

class VDATE:

    server_start = datetime.datetime(2018, 5, 30, 6, 50)

    def boss_darknight(self):
        print "boss_darknight"
        for i in range(0, 30):
            print self.server_start + i*datetime.timedelta(hours = 7)

    def boss_rikanteu(self):
        print "boss_rikanteu"
        for i in range(0, 20):
            print self.server_start + i*datetime.timedelta(hours = 10)

    def boss_gast(self):
        print "gast"
        for i in range(0, 50):
            print self.server_start + i*datetime.timedelta(hours = 3)



    def getCurrentUnixTime(self):
        return time.time()

    def getToday(self):
        return datetime.date.today()

    def getFirstDayOfTheMonth(self):
        return datetime.date.today().replace(day=1)

    def getDateInterval(self):
        return datetime.date.today() - datetime.date.today().replace(day=1)




vdate = VDATE()

vdate.boss_darknight()
vdate.boss_rikanteu()
vdate.boss_gast()
