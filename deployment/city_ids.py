import numpy as np
import pandas as pd

def get_cityid(state, city_name):

    # file_location = "C:/Users/biraj/Documents/company/glassdoor/data"
    
    # Reading the location data to get the city id corresponding to the city name and state
    table = pd.read_csv("../data/location.csv")

    # Converting to lower case 
    state = state.lower()
    city_name = city_name.lower()

    try:
        # Look-up
        cityid = table.loc[(table['City_Name'].str.lower() == city_name)&(table['State_Name'].str.lower() == state), 'City_ID'].values[0]
        return cityid
    except:
        #print("City Id not found !")
        return '0'

    