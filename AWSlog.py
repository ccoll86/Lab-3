#import URL and create local copy of log
import urllib.request 
urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "aws.log")
file = open("aws.log", "r")
URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
Local_copy = 'aws.log'
import os
from datetime import datetime

#defining variables and finding the information in local copy of log
total_requests = 0
last_year_requests = 0

for line in file:
   total_requests += 1
   if line.find("1994")!= -1:
      last_year_requests += 1
file.close()

#print final results found in log
print("This is how many requests in the log file were created ONLY within the last year (1995): ", last_year_requests)

print("This is how many TOTAL requests were created in the entire log file: ", total_requests)
