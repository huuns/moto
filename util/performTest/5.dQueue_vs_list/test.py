#!/usr/bin/python
# -*- coding:utf-8 -*-
################################
###### moto : 2015.07.10 #######
################################

import time
from collections import deque

def listAppend():
  tList = []
  for i in range(0, 10000000):
    tList.append(i)

def listAppend_LC():
  tList = [i for i in range(0, 10000000)]

def listPop(tList):
  for i in range(0, len(tList)):
    tList.pop()
  #while tList:
  #  tList.pop()

def dqueueAppend():
  dQ = deque()
  for i in range(0, 10000000):
    dQ.append(i)

def dqueuePop(tQueue):
  for i in range(0, len(tQueue)):
    tQueue.pop()
  #while tQueue:
  #  tQueue.pop()

if __name__ == "__main__":
  start = time.time()
  listAppend()
  end   = time.time()
  print "list.append() execute time %f seconds" % (end-start)

  start = time.time()
  listAppend_LC()
  end   = time.time()
  print "list.append() LC execute time %f seconds" % (end-start)

  start = time.time()
  dqueueAppend()
  end   = time.time()
  print "dqueue.append() execute time %f seconds" % (end-start)  

  tList = [i for i in range(0, 10000000)]
  start = time.time()
  listPop(tList)
  end   = time.time()
  print "list.pop() execute time %f seconds" % (end-start)  
  
  dQ = deque() 
  for i in range(0, 10000000):
    dQ.append(i)
  start = time.time()
  dqueuePop(dQ)
  end   = time.time()
  print "dqueue.pop() execute time %f seconds" % (end-start)  



