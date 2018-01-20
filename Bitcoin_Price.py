
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

price = pd.read_csv('bitcoin_price.csv')

trade_volume = pd.read_csv('trade_volume.csv')

#split out the last part, which is the year
def get_year(x):
    Date = x.split("/")
    year = Date[2]
    return year 

price['year'] = price.Date.apply(get_year)
price.head()


#find the mean price in each year

price_group = price["Price"].groupby(price["year"]).mean()

price_df = price_group.reset_index()
price_df 

#convert to numeric
price_df["year"] = pd.to_numeric(price_df["year"], errors='coerce')

#format Year 
price_df["Year"] = 2000 + price_df["year"]

price_df.head()

# Cleaning Trade Volume DF

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
merged_df.drop("year_x", "year_y", inplace=True)

merged_df.head()


#print price chart
merged_df.plot(x="Year", y="Price", kind = 'line', color = 'blue',label = 'Price',alpha = 0.5, grid = True)

plt.xlabel('Years')              
plt.ylabel('Price')
plt.title('Price over Years')    
plt.savefig("price.png")
plt.show()


#print Volume chart
merged_df.plot(x="Year", y="Volume", kind = 'line', color = 'blue',label = 'Volume',alpha = 0.5, grid = True)

plt.xlabel('Years')              
plt.ylabel('Volume (Millions)')
plt.title('Trading Volume over Years') 
plt.savefig("volume.png")
plt.show()
