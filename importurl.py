#retrieving log fles across network and creating new local location for the data
import urllib.request 
urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "aws.log")
file = open("aws.log", "r")
URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
Local_copy = 'aws.log'
import os
import re

#start looking for total log requests
i=0

#finding length of lines
def log_len(file):
    lines = file.readlines()
    with open (Local_copy) as y:
        if (len(Local_copy)>=30):
            for i, l in enumerate (y):
                pass
    return i+1
        
        if not os.path.isfile(Local_copy):
        urlretrieve(URL, Local_copy)   
      
#start looking for log requests made in the last year
def yearly_logs():
    
#Adam's regex   
pattern = r'(.*?) - (.*) \[(.*?)\] \"(.*?) (.*?)\"? (.+?) (.+) (.+)'

lines = open(Local_copy, 'r').readlines()

#finding past year logs
for line in lines:
    match = re.match(pattern, line)

    if not match:
        continue

  import datetime
b=0
x = datetime.datetime.now
y = datetime.datetime(2019, 9, 18)
data = lines.split()
date = data[3][1::].split(':')
    with open (Local_copy) as y:
        if (y<date>=x):
          for b, l in enumerate (y):
             pass
    return b+1
    

print('This is how many log requests have been made total: ', i)
print('This is how many log requests have been made in the past year: ',b)

