# -*- coding: utf-8 -*-

targetStation = '"종로3가"'
extractedFile = './extracted_%s.csv' % (targetStation.replace('"',''))

with open(extractedFile, 'w') as ef:
    with open('./seoul.csv', 'r') as f:
            for idx, line in enumerate(f.readlines()):
                if idx == 0:
                    ef.write(line)
                else:
                    sline = line[:-1].split(',')

                    if sline[2] == targetStation:
                        if sline[1] == '"1호선"':
                            ef.write(line)
