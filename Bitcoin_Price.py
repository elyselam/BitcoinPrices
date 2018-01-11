import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('bitcoin_price.csv')

df.head()


def get_month(x):
    Date = x.split("/")
    month = Date[0]
    return month

def get_day(x):
    Date = x.split("/")
    day = Date[1]
    return day

def get_year(x):
    Date = x.split("/")
    year = Date[2]
    return year
    
    
df['month'] = df.Date.apply(get_month)
df['day'] = df.Date.apply(get_day)
df['year'] = df.Date.apply(get_year)
df.head()


group = df["month"].groupby(df["Value"]).mean

df.groupby('year')['Value'].mean()

grouped_monthly = df.groupby(["year","month"])
# df.head()
grouped_monthly.head()
