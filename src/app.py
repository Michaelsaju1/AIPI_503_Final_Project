import pandas as pd

"""
Read the CSV and clean up the data
"""
def read_data(file):
    df = pd.read_csv(file)
    return df


"""
Run the data pipeline based on the information received from Streamlit
"""
def data_pipeline(data):
    pass


"""
Call the API to calculate the carbon footprint
"""
def carbon_footprint(bytes):
    pass


"""
Display the Streamlit user interface to the user for selecting the data they want to see
"""
def display_streamlit():
    pass


if __name__ == "__main__":
    display_streamlit()
