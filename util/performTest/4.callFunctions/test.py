#!/usr/bin/python
# -*- coding:utf-8 -*-
################################
###### moto : 2015.05.31 #######
################################

import time

number = 0

def manyCallFunction(i):
  global number 
  number = number + i

def callFunction(inputList):
  global number
  for i in inputList:
    number = number + i

def sumFunction(inputList):
  global number 
  number = sum(inputList)


if __name__ == "__main__":
  start = time.time()
  for i in range(0, 10000000):
    manyCallFunction(i)
  end   = time.time()
  print "many call function execute time %f seconds" % (end-start)
  print number

  number = 0

  nList  = [i for i in xrange(0, 10000000)]

  start = time.time()
  callFunction(nList)
  end   = time.time()
  print "call function execute time %f seconds" % (end-start)  
  print number

  number = 0

  start = time.time()
  sumFunction(nList)
  end   = time.time()
  print "sum function execute time %f seconds" % (end-start)  
  print number
