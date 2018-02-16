# -*- coding: utf-8 -*-

# =====================================================================
# write : moto
# latest update : 18.02.16
#
# usage : python time.struct_time.py
#
# =====================================================================




import datetime, time

class TIMESTRUCT:
    def getCurrentUnixTime(self):
        return time.time()

    def getTodayTimetuple(self):
        return datetime.date.today().timetuple()
        
    def getNowTimetuple(self):
        return datetime.datetime.now().timetuple()

    

timestruct = TIMESTRUCT()

print timestruct.getNowTimetuple()
print type(timestruct.getNowTimetuple())

print timestruct.getNowTimetuple().tm_year
print timestruct.getNowTimetuple().tm_mon
print timestruct.getNowTimetuple().tm_mday
print timestruct.getNowTimetuple().tm_hour
print timestruct.getNowTimetuple().tm_min
print timestruct.getNowTimetuple().tm_sec
print timestruct.getNowTimetuple().tm_wday
print timestruct.getNowTimetuple().tm_yday
print timestruct.getNowTimetuple().tm_isdst




