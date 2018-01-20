

```python
# Dependencies
import os.path
import json
import pandas as pd
import urllib.request, json
import matplotlib.pyplot as plt
```


```python
# List the urls for the necessary JSON files
cia_2016 = "https://raw.githubusercontent.com/iancoleman/cia_world_factbook_api/master/data/2017-12-25_factbook.json"
cia_2015 = "https://raw.githubusercontent.com/elyselam/CryptoPortfolio/master/2016-12-26_factbook.json"
cia_2014 = "https://raw.githubusercontent.com/elyselam/CryptoPortfolio/master/2015-12-28_factbook.json"
cia_2013 = "https://raw.githubusercontent.com/elyselam/CryptoPortfolio/master/2014-12-29_factbook.json"
cia_2012 = "https://raw.githubusercontent.com/elyselam/CryptoPortfolio/master/2013-12-30_factbook.json"
cia_2011 = "https://raw.githubusercontent.com/elyselam/CryptoPortfolio/master/2012-12-31_factbook.json"
cia_2010 = "https://raw.githubusercontent.com/elyselam/CryptoPortfolio/master/2011-12-26_factbook.json"
cia_2009 = "https://raw.githubusercontent.com/elyselam/CryptoPortfolio/master/2010-12-27_factbook.json"
url_list = [cia_2009, cia_2010, cia_2011, cia_2012, cia_2013, cia_2014, cia_2015, cia_2016]
```


```python
# Create dictionaries to capture desired data
cia_countries = {}
country_desired = ["china","japan","korea_south","united_states", "world"]
```


```python
# Create a DataFrame
cia_dataframe = pd.DataFrame()
```


```python
# Loop through the JSON by desired country and extract desired data for the new dicitonary
for each_url in url_list:
    with urllib.request.urlopen(each_url) as url:
        factfile = json.loads(url.read().decode())
    for country in country_desired:
        data_items = factfile["countries"][country]["data"]
        cia_countries = {
            "Country Name": factfile["countries"][country]["data"]["name"],
            "Year": int(data_items["economy"]["gdp"]["purchasing_power_parity"]["annual_values"][0]["date"]),
            "Population": int(data_items["people"]["population"]["total"]),
            "GDP": int(data_items["economy"]["gdp"]["purchasing_power_parity"]["annual_values"][0]["value"]),
            "GDP per Capita": int(data_items["economy"]["gdp"]["per_capita_purchasing_power_parity"]\
                                        ["annual_values"][0]["value"]),
            "GDP Real Growth Rate": float(data_items["economy"]["gdp"]["real_growth_rate"]["annual_values"][0]["value"]),
            "Unemployment Rate": float(data_items["economy"]["unemployment_rate"]["annual_values"][0]["value"]),
            "Inflation Rate": float(data_items["economy"]["inflation_rate"]["annual_values"][0]["value"]),
            }
        cia_dataframe = cia_dataframe.append(pd.DataFrame(cia_countries, index=[0]), ignore_index=True)
```


```python
# Order the columns, sort the rows, and then reindex the dataframe
cia_ordered_df = cia_dataframe[["Country Name", "Year", "Population", "GDP", "GDP per Capita",\
                                 "GDP Real Growth Rate", "Inflation Rate", "Unemployment Rate"]]
cia_sorted_df = cia_ordered_df.sort_values(by=["Country Name", "Year"])
cia_sorted_df.reset_index(inplace=True)
cia_sorted_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>Country Name</th>
      <th>Year</th>
      <th>Population</th>
      <th>GDP</th>
      <th>GDP per Capita</th>
      <th>GDP Real Growth Rate</th>
      <th>Inflation Rate</th>
      <th>Unemployment Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>China</td>
      <td>2009</td>
      <td>1330141295</td>
      <td>8818000000000</td>
      <td>6700</td>
      <td>9.1</td>
      <td>-0.7</td>
      <td>4.3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>China</td>
      <td>2010</td>
      <td>1336718015</td>
      <td>10090000000000</td>
      <td>7600</td>
      <td>10.3</td>
      <td>3.2</td>
      <td>4.3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10</td>
      <td>China</td>
      <td>2011</td>
      <td>1343239923</td>
      <td>11300000000000</td>
      <td>8400</td>
      <td>9.2</td>
      <td>5.5</td>
      <td>6.5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>China</td>
      <td>2012</td>
      <td>1349585838</td>
      <td>12610000000000</td>
      <td>9300</td>
      <td>7.8</td>
      <td>2.6</td>
      <td>6.5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>20</td>
      <td>China</td>
      <td>2013</td>
      <td>1355692576</td>
      <td>13390000000000</td>
      <td>9800</td>
      <td>7.7</td>
      <td>2.6</td>
      <td>4.1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>25</td>
      <td>China</td>
      <td>2014</td>
      <td>1367485388</td>
      <td>18090000000000</td>
      <td>13200</td>
      <td>7.3</td>
      <td>2.0</td>
      <td>4.1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>30</td>
      <td>China</td>
      <td>2015</td>
      <td>1373541278</td>
      <td>19390000000000</td>
      <td>14100</td>
      <td>6.9</td>
      <td>1.5</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>35</td>
      <td>China</td>
      <td>2016</td>
      <td>1379302771</td>
      <td>21290000000000</td>
      <td>15400</td>
      <td>6.7</td>
      <td>2.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1</td>
      <td>Japan</td>
      <td>2009</td>
      <td>126804433</td>
      <td>4149000000000</td>
      <td>32600</td>
      <td>-5.2</td>
      <td>-1.4</td>
      <td>5.1</td>
    </tr>
    <tr>
      <th>9</th>
      <td>6</td>
      <td>Japan</td>
      <td>2010</td>
      <td>126475664</td>
      <td>4309999999999</td>
      <td>34000</td>
      <td>3.9</td>
      <td>-0.7</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11</td>
      <td>Japan</td>
      <td>2011</td>
      <td>127368088</td>
      <td>4444000000000</td>
      <td>34700</td>
      <td>-0.8</td>
      <td>-0.3</td>
      <td>4.6</td>
    </tr>
    <tr>
      <th>11</th>
      <td>16</td>
      <td>Japan</td>
      <td>2012</td>
      <td>127253075</td>
      <td>4704000000000</td>
      <td>36900</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>4.4</td>
    </tr>
    <tr>
      <th>12</th>
      <td>21</td>
      <td>Japan</td>
      <td>2013</td>
      <td>127103388</td>
      <td>4729000000000</td>
      <td>37100</td>
      <td>2.0</td>
      <td>0.2</td>
      <td>4.1</td>
    </tr>
    <tr>
      <th>13</th>
      <td>26</td>
      <td>Japan</td>
      <td>2014</td>
      <td>126919659</td>
      <td>4767000000000</td>
      <td>37500</td>
      <td>-0.1</td>
      <td>2.7</td>
      <td>3.6</td>
    </tr>
    <tr>
      <th>14</th>
      <td>31</td>
      <td>Japan</td>
      <td>2015</td>
      <td>126702133</td>
      <td>4830000000000</td>
      <td>38100</td>
      <td>0.5</td>
      <td>0.8</td>
      <td>3.4</td>
    </tr>
    <tr>
      <th>15</th>
      <td>36</td>
      <td>Japan</td>
      <td>2016</td>
      <td>126451398</td>
      <td>5233000000000</td>
      <td>41200</td>
      <td>1.0</td>
      <td>-0.1</td>
      <td>3.1</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2</td>
      <td>Korea, South</td>
      <td>2009</td>
      <td>48636068</td>
      <td>1362000000000</td>
      <td>28100</td>
      <td>0.2</td>
      <td>2.8</td>
      <td>3.7</td>
    </tr>
    <tr>
      <th>17</th>
      <td>7</td>
      <td>Korea, South</td>
      <td>2010</td>
      <td>48754657</td>
      <td>1459000000000</td>
      <td>30000</td>
      <td>6.1</td>
      <td>3.0</td>
      <td>3.7</td>
    </tr>
    <tr>
      <th>18</th>
      <td>12</td>
      <td>Korea, South</td>
      <td>2011</td>
      <td>48860500</td>
      <td>1554000000000</td>
      <td>31200</td>
      <td>3.6</td>
      <td>4.0</td>
      <td>3.4</td>
    </tr>
    <tr>
      <th>19</th>
      <td>17</td>
      <td>Korea, South</td>
      <td>2012</td>
      <td>48955203</td>
      <td>1640000000000</td>
      <td>32800</td>
      <td>2.0</td>
      <td>2.2</td>
      <td>3.2</td>
    </tr>
    <tr>
      <th>20</th>
      <td>22</td>
      <td>Korea, South</td>
      <td>2013</td>
      <td>49039986</td>
      <td>1666000000000</td>
      <td>33200</td>
      <td>2.8</td>
      <td>1.1</td>
      <td>3.2</td>
    </tr>
    <tr>
      <th>21</th>
      <td>27</td>
      <td>Korea, South</td>
      <td>2014</td>
      <td>49115196</td>
      <td>1781000000000</td>
      <td>35300</td>
      <td>3.3</td>
      <td>1.3</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>22</th>
      <td>32</td>
      <td>Korea, South</td>
      <td>2015</td>
      <td>50924172</td>
      <td>1849000000000</td>
      <td>36500</td>
      <td>2.6</td>
      <td>0.7</td>
      <td>3.6</td>
    </tr>
    <tr>
      <th>23</th>
      <td>37</td>
      <td>Korea, South</td>
      <td>2016</td>
      <td>51181299</td>
      <td>1934000000000</td>
      <td>37700</td>
      <td>2.8</td>
      <td>1.0</td>
      <td>3.7</td>
    </tr>
    <tr>
      <th>24</th>
      <td>3</td>
      <td>United States</td>
      <td>2009</td>
      <td>310232863</td>
      <td>14120000000000</td>
      <td>46000</td>
      <td>-2.6</td>
      <td>-0.3</td>
      <td>9.3</td>
    </tr>
    <tr>
      <th>25</th>
      <td>8</td>
      <td>United States</td>
      <td>2010</td>
      <td>313232044</td>
      <td>14660000000000</td>
      <td>47200</td>
      <td>2.8</td>
      <td>1.6</td>
      <td>9.6</td>
    </tr>
    <tr>
      <th>26</th>
      <td>13</td>
      <td>United States</td>
      <td>2011</td>
      <td>313847465</td>
      <td>15080000000000</td>
      <td>48300</td>
      <td>1.8</td>
      <td>3.1</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>18</td>
      <td>United States</td>
      <td>2012</td>
      <td>316668567</td>
      <td>15940000000000</td>
      <td>50700</td>
      <td>2.2</td>
      <td>2.1</td>
      <td>8.1</td>
    </tr>
    <tr>
      <th>28</th>
      <td>23</td>
      <td>United States</td>
      <td>2013</td>
      <td>318892103</td>
      <td>16719999999999</td>
      <td>52800</td>
      <td>1.6</td>
      <td>1.5</td>
      <td>7.3</td>
    </tr>
    <tr>
      <th>29</th>
      <td>28</td>
      <td>United States</td>
      <td>2014</td>
      <td>321368864</td>
      <td>17350000000000</td>
      <td>54400</td>
      <td>2.4</td>
      <td>1.6</td>
      <td>6.2</td>
    </tr>
    <tr>
      <th>30</th>
      <td>33</td>
      <td>United States</td>
      <td>2015</td>
      <td>323995528</td>
      <td>17950000000000</td>
      <td>55800</td>
      <td>2.4</td>
      <td>0.1</td>
      <td>5.3</td>
    </tr>
    <tr>
      <th>31</th>
      <td>38</td>
      <td>United States</td>
      <td>2016</td>
      <td>326625791</td>
      <td>18620000000000</td>
      <td>57600</td>
      <td>1.5</td>
      <td>1.3</td>
      <td>4.9</td>
    </tr>
    <tr>
      <th>32</th>
      <td>4</td>
      <td>World</td>
      <td>2009</td>
      <td>6768181146</td>
      <td>70170000000000</td>
      <td>10400</td>
      <td>-0.7</td>
      <td>0.0</td>
      <td>8.7</td>
    </tr>
    <tr>
      <th>33</th>
      <td>9</td>
      <td>World</td>
      <td>2010</td>
      <td>6928198253</td>
      <td>74540000000000</td>
      <td>11200</td>
      <td>4.9</td>
      <td>2.5</td>
      <td>8.7</td>
    </tr>
    <tr>
      <th>34</th>
      <td>14</td>
      <td>World</td>
      <td>2011</td>
      <td>7021836029</td>
      <td>79390000000000</td>
      <td>11900</td>
      <td>3.7</td>
      <td>5.0</td>
      <td>9.1</td>
    </tr>
    <tr>
      <th>35</th>
      <td>19</td>
      <td>World</td>
      <td>2012</td>
      <td>7095217980</td>
      <td>84970000000000</td>
      <td>12700</td>
      <td>3.0</td>
      <td>4.1</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>36</th>
      <td>24</td>
      <td>World</td>
      <td>2013</td>
      <td>7174611584</td>
      <td>87250000000000</td>
      <td>13100</td>
      <td>2.9</td>
      <td>3.9</td>
      <td>8.4</td>
    </tr>
    <tr>
      <th>37</th>
      <td>29</td>
      <td>World</td>
      <td>2014</td>
      <td>7256490011</td>
      <td>109300000000000</td>
      <td>16400</td>
      <td>3.3</td>
      <td>3.8</td>
      <td>8.3</td>
    </tr>
    <tr>
      <th>38</th>
      <td>34</td>
      <td>World</td>
      <td>2015</td>
      <td>7323187457</td>
      <td>114200000000000</td>
      <td>15700</td>
      <td>3.0</td>
      <td>3.6</td>
      <td>8.3</td>
    </tr>
    <tr>
      <th>39</th>
      <td>39</td>
      <td>World</td>
      <td>2016</td>
      <td>7405107650</td>
      <td>120200000000000</td>
      <td>16400</td>
      <td>3.0</td>
      <td>4.6</td>
      <td>7.8</td>
    </tr>
  </tbody>
</table>
</div>




```python
cia_sorted_df.to_csv("cia_data_file.csv")
```


```python
# Import additional dependency
from datetime import datetime
```


```python
# Set the path for the Quandl currency index API
currency_index_path = "https://www.quandl.com/api/v3/datasets/FED/JRXWTFN_N_M.csv?api_key=gCbbx12SgGv9SA8ZeufN"

```


```python
# Read the CSV into a DataFrame
currency_index_df = pd.read_csv(currency_index_path)
#for col in currency_index_df.columns:
#    if currency_index_df[col].dtype == 'object':
#        try:
#            currency_index_df[col] = pd.to_datetime(currency_index_df[col])
#        except ValueError:
#            pass
currency_index_df.head(10)
#currency_index_df.dtypes
```
