#retrieving log fles across network and creating new local location for the data
from urllib.request import urlretrieve
URL_PATH="https://s3.amazonaws.com/tcmg476/http_access_log"
Local_Copy='aws.log'
headers=urlretrieve(URL_PATH, Local_Copy)


#reading file to look for 2 patterns
result1={}
result2={}
total_log_requests=0
past_year_requests=0

file = open("aws.log", "r")

#start looking for total log requests
lines = file.readlines()
import re
for line in lines:
    if re.search('GET', line):
        print('The requests made total: ', line) 

#start looking for log requests made in the last year
lines = file.read
import datetime 
now = datetime.datetime.now
earlier = datetime.datetime(2019, 9, 17)

for lines in file:
    data = lines.split()
    date = data[3][1::].split(':')
    if re.search(earlier>date<=now, line):
        print('The requests made last year: ', line)



