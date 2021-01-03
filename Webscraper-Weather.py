#importing libraries
import requests
from bs4 import BeautifulSoup as soup
import pandas as pd

#url
url ='https://mausam.imd.gov.in/'

#requesting and parsing html
page = requests.get(url)
soup = soup(page.content,'html.parser')

#saving all data into container
container = soup.find_all(class_ = 'capital')

#saving each values in separate arrays
Places = [item.h3.text for item in container]
Temp = [item.find(class_ = 'now').get_text() for item in container]
Wind = [item.find(class_ = 'wind').get_text() for item in container]

#converting to dataframe
Weather_data = pd.DataFrame({
                            'Places':Places,
                            'Temperature':Temp,
                            'Wind':Wind
                            })

#coverting to csv
Weather_data.to_csv('Weather.csv')

