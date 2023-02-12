           # API CALL
#======================================

import time
import requests
import json
import datetime

with open('APIkey.txt') as f:
   api_key = f.readline()
api_key = api_key.strip()

with open('city.txt') as f:
    city = f.readline()
city = city.strip()

url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric" % (city, api_key)  #Get city and units from api


def get_temperature(data):         #outside temp convert to float also determine under which topics data can be found in API request
    return '{:.2f}'.format(data["main"]["temp"]) + ' C'


def run_request(url):                  

    while(True):                         #constantly run request and save it to variable data
        response = requests.get(url)
        data = json.loads(response.text)

        temp1 = get_temperature(data)

        time.sleep(1)    # Important to have some delay, since API calls can only be made 1000 per day.
        return temp1


def write_to_file():

    f = open('dataFile.tsv','a') # open file if it does not exist

    
    #time_stamp = time.time()
    temperature = run_request(url) # read the temperature
    #date_stamp = datetime.date()
    
    time_stamp= time.localtime() # get struct_time
    date_stamp = time.strftime("%m/%d/%Y, %H:%M:%S", time_stamp) #make it readable
    f.write(str(date_stamp) + "\t"+ str(temperature)+ "\n") # write it to the file 
    f.closed # close the file
    
  



if __name__ == '__main__':

    while True:

        run_request(url)
        write_to_file()
        print (run_request(url)) # for debugging
      
      
      
