#!/usr/bin/python
# -*- coding:utf-8 -*-
################################
###### moto : 2015.06.01 #######
################################


#--------------------------------------------------------------------
# format : *.jmx 
# type : text
# data : JMeter - Listner - jp@gc - Response Times Over Time
# example data : 
#                1 1433137160754,1290,pr2_25km2,200,OK,Thread Group 1-3,text,true,415,10,10,http://192.168.0.55/sampleTest/,1290
#                2 1433137160774,1290,pr2_25km2,200,OK,Thread Group 1-8,text,true,415,10,10,http://192.168.0.55/sampleTest/,1290
#                3 1433137160783,1281,pr2_25km2,200,OK,Thread Group 1-5,text,true,415,10,10,http://192.168.0.55/sampleTest/,1280
#                4 1433137160790,1274,pr2_25km2,200,OK,Thread Group 1-2,text,true,415,10,10,http://192.168.0.55/sampleTest/,1274
#                5 1433137160756,2312,pr2_25km2,200,OK,Thread Group 1-1,text,true,415,10,10,http://192.168.0.55/sampleTest/,2312
#                6 1433137160778,2294,pr2_25km2,200,OK,Thread Group 1-7,text,true,415,10,10,http://192.168.0.55/sampleTest/,2294
#                7 1433137160787,2282,pr2_25km2,200,OK,Thread Group 1-9,text,true,415,10,10,http://192.168.0.55/sampleTest/,2282
#                8 1433137160761,2310,pr2_25km2,200,OK,Thread Group 1-4,text,true,415,10,10,http://192.168.0.55/sampleTest/,2310
#                9 1433137160783,2291,pr2_25km2,200,OK,Thread Group 1-10,text,true,415,10,10,http://192.168.0.55/sampleTest/,2290
#--------------------------------------------------------------------

import time

def responseTimeParsing():
  f = open("/home/moto/R/imageFusion_in_188Cloud/data/0601_Threshold_10User.jmx" , "r")
  rf = open("/home/moto/R/imageFusion_in_188Cloud/data/0601_Threshold_10User_ResponseTime.txt" , "w")

  readLines = f.readlines()
  [rf.write(line[line.rfind(",")+1:]) for line in readLines]

  f.close()
  rf.close()

if __name__ == "__main__":
  start = time.time()
  responseTimeParsing()
  end   = time.time()
  print "parsing execute time %f seconds" % (end-start)
