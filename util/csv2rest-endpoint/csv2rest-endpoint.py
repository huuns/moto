# -*- coding: utf-8 -*-

# =====================================================================
# write : moto
# latest update : 16.10.31.
#
# usage : python csv2rest-endpoint.py
#
# rest api end point : 'http://localhost:8000/management/smartphone/'
#
# example : curl -H "Content-Type:application/json" -X POST -d '{"name_kr":"aaa", "name_en":"fff", "maker_code":111}' -u dbuser_name:dbuser_pw http://localhost:8000/management/smartphone/
# =====================================================================



from os import popen

with open("phonelist1031.csv", "r") as f:

    for i, line in enumerate(f):
        if i == 0:
            info = line[:-2].split(",")
            continue

        si = line.splitlines()[0].split(",")

        inputData = []

        for idx, columnName in enumerate(info):
            value = si[idx].replace('"', '')
            inputString = '"%s":"%s"' % (columnName, value)
            inputData.append(inputString)

        csv2rest_endpoint_string = 'curl -H "Content-Type:application/json" -X POST -d '\
                                   ' \'{%s }\' '\
                                   ' -u dbuser_name:dbuser_pw http://localhost:8000/management/smartphone/'\
                                   % ( ", ".join(inputData) )

        popen(csv2rest_endpoint_string)
