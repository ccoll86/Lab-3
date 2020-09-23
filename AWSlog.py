#import URL and create local copy of log
import urllib.request 
urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "aws.log")
file = open("aws.log", "r")
URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
Local_copy = 'aws.log'
import os
import re
import collections
from datetime import datetime

#defining variables and finding the information in local copy of log
all_requests = 0
ly_requests = 0
redirect = 0
error = 0

#finding amount of requests in file by line reading/finding requests made in 1995 (within last year)
for line in file:
   all_requests += 1
   if line.find("1994")!= -1:
      ly_requests += 1

#finding most and least common
def common():
   lcommon=[]
   log=[]
   counter=collections.counter(log)
   
   with open(Local_copy) as logs:
      for line in logs:
         log.append(line[line.index("GET")+4:line.index("HTTP")])
         return
      for 
    
      

#print final results found in log file
print("This is how many requests in the log file were created ONLY within the last year (1995): ", ly_requests)

print("This is how many TOTAL requests were created in the entire log file: ", all_requests)
