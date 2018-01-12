# Dependencies
import os.path
import json
import pandas as pd
import urllib.request, json

# Set a path for the JSON file and read it
cia_url = "https://raw.githubusercontent.com/iancoleman/cia_world_factbook_api/master/data/2017-12-25_factbook.json"
with urllib.request.urlopen(cia_url) as url:
    factfile = json.loads(url.read().decode())

# Create a dictionary to capture desired data
cia_countries = {}

# Loop through the JSON by country and extract desired data for the new dicitonary
for country in factfile["countries"]:
    try:
        data_items = factfile["countries"][country]["data"]
        cia_countries[country] = {
            "Country Name": factfile["countries"][country]["data"]["name"],
            "Population": int(data_items["people"]["population"]["total"]),
            "Internet Users": int(data_items["communications"]["internet"]["users"]["total"]),
            "Internet Users (% of Pop)": float(data_items["communications"]["internet"]["users"]["percent_of_population"]),
            "GDP Year (2)": int(data_items["economy"]["gdp"]["purchasing_power_parity"]["annual_values"][0]["date"]),
            "GDP Year (1)": int(data_items["economy"]["gdp"]["purchasing_power_parity"]["annual_values"][1]["date"]),
            "GDP (2)": int(data_items["economy"]["gdp"]["purchasing_power_parity"]["annual_values"][0]["value"]),
            "GDP (1)": int(data_items["economy"]["gdp"]["purchasing_power_parity"]["annual_values"][1]["value"]),
            "GDP per Capita Year (2)": int(data_items["economy"]["gdp"]["per_capita_purchasing_power_parity"]\
                                        ["annual_values"][0]["date"]),
            "GDP per Capita Year (1)": int(data_items["economy"]["gdp"]["per_capita_purchasing_power_parity"]\
                                        ["annual_values"][1]["date"]),
            "GDP per Capita (2)": int(data_items["economy"]["gdp"]["per_capita_purchasing_power_parity"]\
                                        ["annual_values"][0]["value"]),
            "GDP per Capita (1)": int(data_items["economy"]["gdp"]["per_capita_purchasing_power_parity"]\
                                        ["annual_values"][1]["value"]),
            "GDP Real Growth Rate Year (2)": int(data_items["economy"]["gdp"]["real_growth_rate"]["annual_values"][0]["date"]),
            "GDP Real Growth Rate Year (1)": int(data_items["economy"]["gdp"]["real_growth_rate"]["annual_values"][1]["date"]),
            "GDP Real Growth Rate (2)": float(data_items["economy"]["gdp"]["real_growth_rate"]["annual_values"][0]["value"]),
            "GDP Real Growth Rate (1)": float(data_items["economy"]["gdp"]["real_growth_rate"]["annual_values"][1]["value"]),
            "Unemployment Rate Year (2)": int(data_items["economy"]["unemployment_rate"]["annual_values"][0]["date"]),
            "Unemployment Rate Year (1)": int(data_items["economy"]["unemployment_rate"]["annual_values"][1]["date"]),
            "Unemployment Rate (2)": float(data_items["economy"]["unemployment_rate"]["annual_values"][0]["value"]),
            "Unemployment Rate (1)": float(data_items["economy"]["unemployment_rate"]["annual_values"][1]["value"]),
            "Inflation Rate Year (2)": int(data_items["economy"]["inflation_rate"]["annual_values"][0]["date"]),
            "Inflation Rate Year (1)": int(data_items["economy"]["inflation_rate"]["annual_values"][1]["date"]),
            "Inflation Rate (2)": float(data_items["economy"]["inflation_rate"]["annual_values"][0]["value"]),
            "Inflation Rate (1)": float(data_items["economy"]["inflation_rate"]["annual_values"][1]["value"]),
            }
    except:
        pass

# Create a DataFrame
cia_dataframe = pd.DataFrame(cia_countries)
cia_df = cia_dataframe.transpose()

# Order the columns logically
cia_ordered_df = cia_df[["Country Name", "Population", "Internet Users", "Internet Users (% of Pop)", "GDP Year (1)", \
                        "GDP (1)", "GDP Year (2)", "GDP (2)", "GDP per Capita Year (1)", "GDP per Capita (1)", \
                        "GDP per Capita Year (2)", "GDP per Capita (2)", "GDP Real Growth Rate Year (1)", \
                        "GDP Real Growth Rate (1)", "GDP Real Growth Rate Year (2)", "GDP Real Growth Rate (2)", \
                        "Unemployment Rate Year (1)", "Unemployment Rate (1)", "Unemployment Rate Year (2)", \
                        "Unemployment Rate (2)", "Inflation Rate Year (1)", "Inflation Rate (1)", \
                         "Inflation Rate Year (2)", "Inflation Rate (2)"]]
cia_ordered_df.head(3)
