import pandas as pd
import requests
import matplotlib.pyplot as plt
import os

"""
Read the CSV and clean up the data
"""
def read_data(file):
    df = pd.read_csv(file)
    df = df[["bytes", "country"]]
    return df

"""
Takes in a list of countries to call the API and returns a new DataFrame with the relevant data
"""
def process_data(file, countries):
    df = pd.read_csv(file)

    total_bytes_for_countries = df.groupby("country")["bytes"].sum()

    results = []

    for country in countries:
        country_bytes = total_bytes_for_countries[country]
        g2coe, ct, energy = carbon_footprint(country_bytes)
        results.append([country, country_bytes, g2coe, ct, energy])

    results_df = pd.DataFrame(results, columns=["country", "bytes", "gco2e", "ct", "energy"])

    return results_df


"""
Call the API to calculate the carbon footprint
"""
def carbon_footprint(bytes):
    url = f"https://api.websitecarbon.com/data?bytes={bytes}&green=0"

    # Make the request
    response = requests.get(url)

    # Parse JSON
    data = response.json()

    # Extract key info
    return data["gco2e"], data["cleanerThan"], data["statistics"]["energy"]


"""
Uses Matplotlib to plot all of the countries and their g2coe
"""
def plot_country(data):
    # Sort countries by emissions
    top_countries = data.sort_values("gco2e", ascending=False)
    plt.figure(figsize=(10, 5))
    plt.bar(top_countries['country'], top_countries["gco2e"], color="green")
    plt.xlabel("Country Type")
    plt.ylabel("Total CO2 Emissions (g)")
    plt.title("CO2 Emissions by Country Type")
    plt.xticks(rotation=45)
    os.makedirs("../figures", exist_ok=True)
    plt.savefig("../figures/country-plot.png")
