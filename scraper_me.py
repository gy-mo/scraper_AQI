# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 10:41:11 2020

@author: ram
"""

import os 
import time 
import requests
import sys


def retrieve_HTML():
    for year in range(2013,2019):
        for month in range(1,13):
            if month < 10:
                url='https://en.tutiempo.net/climate/0{}-{}/ws-432950.html'.format(month,year)
            else:
                url='https://en.tutiempo.net/climate/{}-{}/ws-432950.html'.format(month,year)
                
            html_data = requests.get(url)
        
            html_data_utf = html_data.text.encode('utf=8')
        
        
            if not os.path.exists('/data_aqi/Html_Data/{}'.format(year)):
                os.makedirs('/data_aqi/Html_Data/{}'.format(year))
            with open("/data_aqi/Html_Data/{}/{}.html".format(year,month),'wb') as output:
                output.write(html_data_utf)
        sys.stdout.flush()
        
   

if  __name__ == "__main__":
    start_time=time.time()
    print(start_time)
    retrieve_HTML()
    stop_time = time.time()
    print(stop_time)
    print('time taken: {}'.format(stop_time-start_time))





     