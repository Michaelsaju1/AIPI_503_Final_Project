import pandas as pd

"""
Read the CSV and clean up the data
"""
def read_and_process_data(file):
    df = pd.read_csv(file)

    # delete columns we don't need
    del df["duration_(secs)"]
    del df["network_protocol"]
    del df["ip"]
    del df["accessed_date"]

    # TODO: group the df by country or other user input

    for i, row in df.iterrows():
        bytes = row["bytes"]
        carbon_footprint_response = carbon_footprint(bytes)
        

"""
Call the API to calculate the carbon footprint
"""
def carbon_footprint(bytes):
    pass


"""
Run the data pipeline based on the information received from Streamlit
"""
def data_pipeline(data):
    pass


"""
Display the Streamlit user interface to the user for selecting the data they want to see
"""
def display_streamlit():
    df = read_and_process_data("../data/ecommerce-website-logs.csv")


if __name__ == "__main__":
    display_streamlit()
