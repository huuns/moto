#!/usr/bin/python
# -*- coding:utf-8 -*-
################################
###### moto : 2015.05.31 #######
################################

import time
import math

def generatorExpression():
  nList = [i for i in xrange(0, 10000000)]
  mList = []
  
  mList = (math.sqrt(n) for n in nList)
  

def generatorExpressionAndEliminateDots():
  nList = [i for i in xrange(0, 10000000)]
  mList = []
  
  sqrt = math.sqrt
  mList = (sqrt(n) for n in nList)


if __name__ == "__main__":
  start = time.time()
  generatorExpression()
  end   = time.time()
  print "generatorExpression execute time %f seconds" % (end-start)

  start = time.time()
  generatorExpressionAndEliminateDots()
  end   = time.time()
  print "generatorExpression and Eliminate Dots execute time %f seconds" % (end-start)
