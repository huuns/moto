# -*- coding: utf-8 -*-

# =====================================================================
# write : moto
# latest update : 17.05.24.
#
# parsing --> db --> csv --> s3
# viewing --> s3
#
# =====================================================================

import sys
from robobrowser import RoboBrowser

reload(sys)
sys.setdefaultencoding('utf-8')


class WEBPARSER:

    def getData(self):

        browser = RoboBrowser(history=True,
            user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/33.0.1750.152 Chrome/33.0.1750.152 Safari/537.36')

        # lezhin login ----------------------------------------------------------------- start
        browser.open('https://www.lezhin.com/ko/login')
        form = browser.get_form(id='login-form')
        form['username'].value = '2kjldkjslkjfr23@naver.com'
        form['password'].value = ';dlfkjlakjrl3k2lkjlfkjaldksjflaksjdflkdf'
        browser.submit_form(form)
        # lezhin login ----------------------------------------------------------------- end



        # lezhin parsing --------------------------------------------------------------- start
        url_content = 'https://www.lezhin.com/ko/library'
        browser.open(url_content)
        mylibrary_li = browser.find_all('li', class_='comic')
        print mylibrary_li
        # lezhin parsing --------------------------------------------------------------- end


tt = WEBPARSER()
tt.getData()
