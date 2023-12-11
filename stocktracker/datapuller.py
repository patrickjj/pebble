import requests
import json

import pandas as pd

sp_df = pd.read_csv('constituents.csv')


#list of s&p 500 companies from here: https://datahub.io/core/s-and-p-500-companies
# using api docs found here: https://www.alphavantage.co/documentation/
config_dict = {}
with open("api.config") as file:
    for line in file:
       (key, val) = line.split("=")
       config_dict[key] = val

print(sp_df.head())
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&outputsize=compact&symbol=IBM&apikey=' + config_dict["key"]
r = requests.get(url)
data = r.json()
with open('data.json', 'w') as f:
    json.dump(data, f)

print(data)