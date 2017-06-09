# -*- coding: utf-8 -*-

# =====================================================================
# write : moto
# latest update : 17.05.24.
#
# parsing --> db --> csv --> s3
# viewing --> s3
#
# =====================================================================

import datetime, sys, sqlite3, json
from robobrowser import RoboBrowser
from dbconn import DBCONN
from os import popen

reload(sys)
sys.setdefaultencoding('utf-8')


from tracker_lezhin import TRACKER_LEZHIN
from tracker_toomics import TRACKER_TOOMICS
from tracker_ktoon import TRACKER_KTOON
from tracker_foxtoon import TRACKER_FOXTOON


def processing(obj):
    obj.getData()
    obj.updateTable()
    obj.jsonCreate2s3()
    obj.onecoin_price_jsonCreate2s3()


lezhin = TRACKER_LEZHIN()
processing(lezhin)

toomics = TRACKER_TOOMICS()
processing(toomics)

ktoon = TRACKER_KTOON()
processing(ktoon)

foxtoon = TRACKER_FOXTOON()
processing(foxtoon)
