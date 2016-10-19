# -*- coding:utf-8 -*-

import requests

class KAKAO_ID_TOKEN_CHECK:

    def kakao_check(self, kakaoid, token):
        endpoint = "https://kapi.kakao.com/v1/user/access_token_info"
        headers  = {"Authorization":"Bearer %s" % (token) }

        if kakaoid == str(requests.get(endpoint,headers=headers).json()["id"]):
            return True
        else:
            return False

