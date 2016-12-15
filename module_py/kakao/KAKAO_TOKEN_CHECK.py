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


    # GET /v1/user/ids HTTP/1.1
    # Host: kapi.kakao.com
    # Authorization: KakaoAK {admin_key}
    # Content-type: application/x-www-form-urlencoded;charset=utf-8
    def get_kakao_user_list(self, adminToken):
        endpoint = "https://kapi.kakao.com/v1/user/ids"
        headers  = {"Authorization":"KakaoAK %s" % (adminToken) }
        userCount = requests.get(endpoint,headers=headers).json()["total_count"]
        return userCount
        
