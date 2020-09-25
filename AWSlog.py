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

janlogs=open("january.txt", "a+"); feblogs=open("february.txt", "a+"); marlogs=open("march.txt", "a+"); 
aprlogs=open("april.txt", "a+"); maylogs=open("may.txt", "a+"); junlogs=open("june.txt", "a+");
jullogs=open("july.txt", "a+"); auglogs=open("august.txt", "a+"); seplogs=open("september.txt", "a+")
octlogs=open("octlogs.txt", "a+"); novlogs=open("november.txt", "a+"); declogs=open("december.txt", "a+")  

#finding amount of requests in file by line reading/finding requests made in 1995 (within last year)
for line in file:
   all_requests += 1
   if line.find("1994")!= -1:
      ly_requests += 1

#finding most and least common
def fileCount():
	filelog = []
	leastcommon = []
	with open(LOCAL_FILE) as logs:
		for line in logs:
			try:
				filelog.append(line[line.index("GET")+4:line.index("HTTP")])		
			except:
				pass
	counter = collections.Counter(filelog)
	for count in counter.most_common(1):														
		print("Most common file: {} with {} requests.".format(str(count[0]), str(count[1])))
	for count in counter.most_common():					
		if str(count[1]) == '1':
			leastcommon.append(count[0])
	if leastcommon:																						
		response = input("Display files requested only once? Y/N)".format(len(leastcommon)))
		if response == 'y' or response == 'Y':
			for file in leastcommon:
				print(file)
     
#months count and redirect/error count
pattern = r'(.*?) - (.*) \[(.*?)\] \"(.*?) (.*?)\"? (.+?) (.+) (.+)'
lines = open(Local_file, 'r').readlines()


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
     
#print final results found in log file
totalResponses = file_len(Local_file)
print("This is how many requests in the log file were created ONLY within the last year (1995): ", ly_requests)
print("This is how many TOTAL requests were created in the entire log file: ", all_requests)
print("Average number for month:", round(totalResponses/12,2))
print("Average number for week: ",round(totalResponses/52,2))
print("Average number for day: ", round(totalResponses/365,2))
print("Month Count:", months_count)
print("Total number of redirects:",redirectCounter)
print("Percentage of all requests that were redirects (3xx): {0:.2%}".format(redirectCounter/totalResponses))
print("Error count:",errorCounter)
print("Percentage of client error (4xx) requests: {0:.2%}".format(errorCounter/totalResponses))	
