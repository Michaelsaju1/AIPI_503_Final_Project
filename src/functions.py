import pandas as pd
import requests
import matplotlib.pyplot as plt

"""
Read the CSV and clean up the data
"""
def read_data(file):
    df = pd.read_csv(file)
    return df

def read_and_process_data(file, country1, country2):
    df = pd.read_csv(file)
    #print("done reading csv")

    df = df[["bytes","country"]]
    
    total_bytes_for_countries = df.groupby("country")["bytes"].sum()
    bytes_country1 = total_bytes_for_countries[country1]
    bytes_country2 = total_bytes_for_countries[country2]

    co2_country1, ct_country1, energy_country1 = carbon_footprint(bytes_country1)
    co2_country2, ct_country2, energy_country2 = carbon_footprint(bytes_country2)
    
    #print(co2_country1, ct_country1, energy_country1)
    #print(co2_country2, ct_country2, energy_country2)

    total_bytes_for_countries = total_bytes_for_countries.to_frame()
    #print(type(total_bytes_for_countries))
    total_bytes_for_countries.loc[country1, ["gco2e", "ct", "energy"]] = [co2_country1, ct_country1, energy_country1]
    total_bytes_for_countries.loc[country2, ["gco2e", "ct", "energy"]] = [co2_country2, ct_country2, energy_country2]
    
    return total_bytes_for_countries

"""
Call the API to calculate the carbon footprint
"""
def carbon_footprint(bytes):
    url = f"https://api.websitecarbon.com/data?bytes={bytes}&green=0"

    #Make the request
    response = requests.get(url)

    #Parse JSON
    data = response.json()

    #Extract key info
    return data["gco2e"], data["cleanerThan"], data["statistics"]["energy"]


"""
Run the data pipeline based on the information received from Streamlit
"""
def data_pipeline(data):
    pass

def plot_country(data):
    # Sort countries by emissions
    top_countries =data.sort_values("gco2e", ascending=False)
    plt.figure(figsize=(10,5))
    plt.bar(top_countries[""], top_countries["gco2e"], color="green")
    plt.xlabel("Country Type")
    plt.ylabel("Total CO2 Emissions (g)")
    plt.title("CO2 Emissions by Country Type")
    plt.xticks(rotation=45)

