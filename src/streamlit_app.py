import streamlit as st
import functions
from streamlit_chat import message


if "history" not in st.session_state:
    st.session_state.history = []

st.header("Carbon Emmissions by country")
"""
This interface provides useful information to determine the carbon emmissions for the selected country from the user.
"""
st.image(
    "https://www.greengeeks.com/blog/wp-content/uploads/2018/12/CO2-emission_header.jpg",
    caption="Carbon Emmisions",
    use_container_width=True
)

# 2. Run when user presses Enter OR button
user_input = None
submit_button = None

# Input box
df = functions.read_data("../data/ecommerce-website-logs.csv")
user_input = st.multiselect(
    "Please select two cities you would like the Carbon Emmissions for below:",
    df['country'].unique())
submit_button = st.button("Get Carbon Emmissions")

if submit_button:
    country1, country2 = user_input[0], user_input[1]
    #print(country1, country2)
    df = functions.read_and_process_data("../data/ecommerce-website-logs.csv", country1, country2)
    bot_response = (
    f"The Carbon Emissions for {country1} is {df.loc[country1, 'gco2e']:.2f} g/m^3. "
    f"The Carbon Emissions for {country2} is {df.loc[country2, 'gco2e']:.2f} g/m^3."
    )   
    #Do we want to add ct and energy?
    st.session_state.history.append({
        "user": (f"Country 1: {user_input[0]}, Country 2: {user_input[1]}"),
        "bot": bot_response
    })

# 3. Display the chat history

for i, chat in enumerate(st.session_state.history):
    message(chat["user"], is_user=True, key=f"user_{i}")
    message(chat["bot"], key=f"bot_{i}")