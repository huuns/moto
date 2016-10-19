#!/usr/bin/python
# -*- coding:utf-8 -*-
################################
###### moto : 2015.05.31 #######
################################

import time
import math

def forLoops():
  nList = [i for i in xrange(0, 10000000)]
  mList = []  

  for n in nList:
    mList.append(math.sqrt(n))  
  
  
def listComprehensions():
  nList = [i for i in xrange(0, 10000000)]
  mList = []
  
  mList = [math.sqrt(n) for n in nList]


def generatorExpression():
  nList = [i for i in xrange(0, 10000000)]
  mList = []
  
  mList = (math.sqrt(n) for n in nList)
  

if __name__ == "__main__":
  start = time.time()
  forLoops()
  end   = time.time()
  print "forLoops execute time %f seconds" % (end-start)

  start = time.time()
  listComprehensions()
  end   = time.time()
  print "listComprehensions execute time %f seconds" % (end-start)

  start = time.time()
  generatorExpression()
  end   = time.time()
  print "generatorExpression execute time %f seconds" % (end-start)
