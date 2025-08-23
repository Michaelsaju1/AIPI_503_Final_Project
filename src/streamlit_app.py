import streamlit as st
import functions

"""
Display the Streamlit user interface to the user for selecting the data they want to see
"""
feature = st.radio(
    "Pick a column to group by",
    ("Country", "Gender")
)
df = functions.read_and_process_data("../data/ecommerce-website-logs.csv", feature)

st.write("Completed!")