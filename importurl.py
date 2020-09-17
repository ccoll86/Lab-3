#retrieving log fles across network and creating new local location for the data
import urllib.request 
urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "aws.log")
file = open("aws.log", "r")

#start looking for total log requests
def main1():
    total_log_requests=int()
    lines = file.readlines()
    for line in lines:
        if(len(line)>=30):
             total_log_requests+=1
        return total_log_requests
    print('The requests made total: ', total_log_requests) 

#start looking for log requests made in the last year
def main2():
    past_year_requests=int()
    lines = file.readlines()
    import datetime
    import re
    now = datetime.datetime.now
    earlier = datetime.datetime(2019, 9, 17)
    for line in lines:
         data = lines.split()
         date = data[3][1::].split(':')
            if re.search(earlier>date<=now, line):
                  past_year_requests+=1
            return past_year_requests
    print('The requests made last year: ', past_year_requests)



