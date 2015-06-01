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
  f1  = open("/home/ruser/R/imageFusion_in_188Cloud/data/0601_Threshold_10User.jmx" , "r")
  f2  = open("/home/ruser/R/imageFusion_in_188Cloud/data/0601_Threshold_20User.jmx" , "r")
  f3  = open("/home/ruser/R/imageFusion_in_188Cloud/data/0601_Threshold_30User.jmx" , "r")
  f4  = open("/home/ruser/R/imageFusion_in_188Cloud/data/0601_Threshold_40User.jmx" , "r")
  f5  = open("/home/ruser/R/imageFusion_in_188Cloud/data/0601_Threshold_50User.jmx" , "r")

  rf = open("/home/ruser/R/imageFusion_in_188Cloud/data/0601_Threshold_MultipleUser_ResponseTime2.txt" , "w")
 
  rf.write("group, response\n")
  readLines1 = f1.readlines()
  readLines2 = f2.readlines()
  readLines3 = f3.readlines()
  readLines4 = f4.readlines()
  readLines5 = f5.readlines()

  [rf.write("%s, %s" % ("user10" ,line[line.rfind(",")+1:])) for index, line in enumerate(readLines1) if index<1000]
  [rf.write("%s, %s" % ("user20" ,line[line.rfind(",")+1:])) for index, line in enumerate(readLines2) if index<1000]
  [rf.write("%s, %s" % ("user30" ,line[line.rfind(",")+1:])) for index, line in enumerate(readLines3) if index<1000]
  [rf.write("%s, %s" % ("user40" ,line[line.rfind(",")+1:])) for index, line in enumerate(readLines4) if index<1000]
  [rf.write("%s, %s" % ("user50" ,line[line.rfind(",")+1:])) for index, line in enumerate(readLines5) if index<1000]

  f1.close()
  f2.close()
  f3.close()
  f4.close()
  f5.close()
  rf.close()

if __name__ == "__main__":
  start = time.time()
  responseTimeParsing()
  end   = time.time()
  print "parsing execute time %f seconds" % (end-start)
