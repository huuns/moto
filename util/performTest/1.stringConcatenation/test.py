#!/usr/bin/python
# -*- coding:utf-8 -*-
################################
###### moto : 2015.05.31 #######
################################

import time

def stringPlus():
  s = ""
  #stringList = [str(i) for i in range(0, 10000000)]
  stringList = [str(i) for i in xrange(0, 10000000)]
  
  for i in stringList:
    s += i

def stringJoin():
  s = ""
  #stringList = [str(i) for i in range(0, 10000000)]
  stringList = [str(i) for i in xrange(0, 10000000)]
  
  s.join(stringList) 


if __name__ == "__main__":
  start = time.time()
  stringPlus()
  end   = time.time()
  print "string ++++++ execute time %f seconds" % (end-start)

  start = time.time()
  stringJoin()
  end   = time.time()
  print "string join execute time %f seconds" % (end-start)

