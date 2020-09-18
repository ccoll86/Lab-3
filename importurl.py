import urllib.request 
urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "aws.log")
file = open("aws.log", "r")
URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
Local_copy = 'aws.log'
import os

total_requests = 0
last_year_requests = 0
last_line = ""

for line in file:
    total_requests += 1
    if line.find("1994")!= -1:
        last_year_requests += 1
file.close()

print("This is how many log requests were created last year: ", last_year_requests)
print("This is how many total log requests were created in the file: ", total_requests)
