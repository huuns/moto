# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import psycopg2
from bs4 import BeautifulSoup
import urllib2, json, os
from urllib2 import Request, urlopen, URLError, HTTPError

import datetime

HOOK_URL = "https://hooks.slack.com/services/!!!!!!!!!!!!!!!"

page_status = 'message'

alarm_name = "Daily Check (Converse) : Favorite Shoes Detail Page / " + str(datetime.date.today())

slack_message = {
    'channel': "moto_t",
    "mrkdwn": 'true',
    "attachments": [
        {
            "color": "#36a64f",
            "title": alarm_name,
            "text": page_status,
            "footer": "Daily Check Tool (v0.1)",
            "mrkdwn": 'true'
        }
    ]
}

req = Request(HOOK_URL, json.dumps(slack_message))

try:
    response = urlopen(req)
    response.read()
except HTTPError as e:
    print "Request failed: %d %s", e.code, e.reason
except URLError as e:
    print "Server connection failed: %s", e.reason
