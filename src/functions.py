import pandas as pd
import requests

"""
Read the CSV and clean up the data
"""
def read_and_process_data(file, country1, country2):
    df = pd.read_csv(file)
    print("done reading csv")

    df = df[["bytes","country"]]
    
    total_bytes_for_countries = df.groupby("country")["bytes"].sum()
    bytes_country1 = total_bytes_for_countries[country1]
    bytes_country2 = total_bytes_for_countries[country2]

    co2_country1, ct_country1, energy_country1 = carbon_footprint(bytes_country1)
    co2_country2, ct_country2, energy_country2 = carbon_footprint(bytes_country2)
    
    print(co2_country1, ct_country1, energy_country1)
    print(co2_country2, ct_country2, energy_country2)

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


#if __name__ == "__main__":
#   display_streamlit()
