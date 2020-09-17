#retrieving log fles across network and creating new local location for the data
import urllib.request 
urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "aws.log")

#reading file to look for 2 patterns
result1={
    "total_log_requests":0
}
result2={
    "past_year_requests":{}
}

file = open("aws.log", "r")

#start looking for total log requests
lines = file.readlines()
for lines in file:
    if(len(lines)>=56):
        result1["total_log_requests: "]+=1   

#start looking for log requests made in the last year
lines = file.readlines
import datetime 
now = datetime.datetime.now
earlier = datetime.datetime(2019, 9, 17)

for lines in file:
    data = lines.split()
    date = data[3][1::].split(':')
    if(earlier>date<now):
        result2["past_year_requests: "]+=1
 
print(result1)    
print(result2)


