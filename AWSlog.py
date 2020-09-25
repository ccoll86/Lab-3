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

#defining variables, months, and finding the information in local copy of log
all_requests = 0
ly_requests = 0
redirect = 0
error = 0

months_count ={
  "Jan": 0,
  "Feb": 0,
  "Mar": 0,
  "Apr": 0,
  "May": 0,
  "Jun": 0,
  "Jul": 0,
  "Aug": 0,
  "Sep": 0,
  "Oct": 0,
  "Nov": 0,
  "Dec": 0
}

#creating 12 local files for each month and their associated files in the log
janlogs=open("january.txt", "a+"); feblogs=open("february.txt", "a+"); 
marlogs=open("march.txt", "a+"); aprlogs=open("april.txt", "a+"); 
maylogs=open("may.txt", "a+"); junlogs=open("june.txt", "a+");
jullogs=open("july.txt", "a+"); auglogs=open("august.txt", "a+"); 
seplogs=open("september.txt", "a+"); octlogs=open("octlogs.txt", "a+"); 
novlogs=open("november.txt", "a+"); declogs=open("december.txt", "a+")  

#finding amount of requests in file by line reading/finding requests made in 1995 (within last year)
for line in file:
    all_requests += 1
    if line.find("1995") != -1:
        ly_requests += 1

#finding most and least requested(common)
def common():
	flog = []
	lcommon = []
	with open(Local_copy) as logs:
		for line in logs:
			try:
				flog.append(line[line.index("GET")+4:line.index("HTTP")])		
			except:
				pass
	counter = collections.Counter(flog)
	for count in counter.most_common(1):														
		print("Most common file: {} with {} requests.".format(str(count[0]), str(count[1])))
	for count in counter.most_common():					
		if str(count[1]) == '1':
			lcommon.append(count[0])
	if lcommon:																						
		response = input("Display files requested only once? Y/N)".format(len(lcommon)))
		if response == 'y' or response == 'Y':
			for file in lcommon:
				print(file)
     
#months count and redirect/error count with regex pattern
pattern = r'(.*?) - (.*) \[(.*?)\] \"(.*?) (.*?)\"? (.+?) (.+) (.+)'
lines = open(Local_copy, 'r').readlines()

#matching files to months count local files
for line in lines:
    match = re.match(pattern, line)

    if not match:
        continue

    match.group(0) 
    match.group(3) 
    timestamp = match.group(3)
    month = timestamp[3:6]
    months_count[month] += 1
    match.group(7) 
    
    if (match.group(7)[0] == "3"):
        redirect += 1
    elif (match.group(7)[0] == "4"):
        error += 1
    if (month == "Jan"): 
        janlogs.write(line)
    elif (month == "Feb"): 
        feblogs.write(line)
    elif (month == "Mar"): 
        marlogs.write(line)
    elif (month == "Apr"): 
        aprlogs.write(line)
    elif (month == "May"): 
        maylogs.write(line)
    elif (month == "Jun"): 
        junlogs.write(line)
    elif (month == "Jul"): 
        jullogs.write(line)
    elif (month == "Aug"): 
        auglogs.write(line)
    elif (month == "Sep"): 
        seplogs.write(line)
    elif (month == "Oct"): 
        octlogs.write(line)
    elif (month == "Nov"): 
        novlogs.write(line)
    elif (month == "Dec"): 
        declogs.write(line)
    
    else:
        continue

file.close()
     
#print final results found in log file
print('FINAL RESULTS:')
print('TOTAL AND LAST YEAR REQUESTS:')
print("This is how many requests in the log file were created ONLY within the last year (1995): ", ly_requests)
print("This is how many TOTAL requests were created in the entire log file: ", all_requests)
print('AVERAGES:')
print("Average number for one month:", round(all_requests/12,2))
print("Average number for one week: ",round(all_requests/52,2))
print("Average number for one day: ", round(all_requests/365,2))
print("Month Amount:", months_count)
print('REDIRECTS, ERRORS, AND PERCENTAGES:')
print("Total number of redirects:",redirect)
print("Percentage of all requests that were redirects (3xx): {0:.2%}".format(redirect/all_requests))
print("Error count:",error)
print("Percentage of client error (4xx) requests: {0:.2%}".format(error/all_requests))	
print('MOST AND LEAST REQUESTED FILES:')
common()
