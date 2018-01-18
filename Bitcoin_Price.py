import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

price = pd.read_csv('bitcoin_price.csv')

trade_volume = pd.read_csv('trade_volume.csv')

def get_year(x):
    Date = x.split("/")
    year = Date[2]
    return year 

price['year'] = price.Date.apply(get_year)
price.head()


price_group = price["Price"].groupby(price["year"]).mean()

price_df = price_group.reset_index()
price_df 
#convert to numeric
price_df["year"] = pd.to_numeric(price_df["year"], errors='coerce')

#format Year 
price_df["Year"] = 2000 + price_df["year"]

price_df.head()

#delete year column

price_df.drop(["year"], inplace=True)

#CLEAN TRADE_VOLUME FILE
trade_volume['year'] = trade_volume.Date.apply(get_year)
trade_volume.head()


trade_volume_group = trade_volume["Volume"].groupby(price["year"]).mean()

trade_volume_df = trade_volume_group.reset_index()
trade_volume_df 


#convert to numeric
trade_volume_df["year"] = pd.to_numeric(trade_volume_df["year"], errors='coerce')


#format Year 
trade_volume_df["Year"] = 2000 + trade_volume_df["year"]

trade_volume_df


merged_df = pd.merge(price_df, trade_volume_df, on="Year")
merged_df


#drop year column
merged_df.drop("year", inplace=True, axis=1)
merged_df.head()
