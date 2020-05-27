import pandas as pd 
import requests 
from bs4 import BeautifulSoup
import numpy as np 
import matplotlib.pyplot as plt 


page = requests.get('https://www.metoffice.gov.uk/weather/forecast/gcnk62de6#?date=2020-05-27')
soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(id='dayNav')

days = week.find_all(class_='tab-day')
high_temp = week.find_all(class_='tab-temp-high')
low_temp = week.find_all(class_='tab-temp-low')
summary = week.find_all(class_='summary-text hide-xs-only')

day_titles = [day.get_text().replace('\n','') for day in days]
high_temperatures = [temp.get_text() for temp in high_temp]
low_temperatures = [temp.get_text() for temp in low_temp]
summary_stat = [item.get_text().replace('\n','') for item in summary] 

weather_stuff = pd.DataFrame(
	{'days':day_titles,'high_temp':high_temperatures,
	'low_temp': low_temperatures, 'summary': summary_stat})

weather_stuff.to_csv('/Users/amitkamlani/Desktop/','Bath Weather.csv') 

day_array = np.array(day_titles)
high_temp_array = np.array(high_temperatures)
low_temp_array = np.array(low_temperatures) 

plt.plot(day_array,high_temp_array,low_temp_array)



