import streamlit as st
import functions
from streamlit_chat import message

if "history" not in st.session_state:
    st.session_state.history = []

st.header("Carbon Emissions by Country")
"""
This project calculates the carbon emission for countries you select from the dataset. A list of user sessions for a
popular e-commerce website is the dataset we used. We group by the country and calculate the sum to determine the total
amount of bytes used for each country. Our API is a carbon emissions calculator that takes in the total amount of bytes
per country. It gives the Total CO2 emissions in grams, the percentage of websites it is cleaner than, and the energy
used per each country.
"""
st.image(
    "https://www.greengeeks.com/blog/wp-content/uploads/2018/12/CO2-emission_header.jpg",
    caption="Carbon Emissions",
    use_container_width=True
)

# 2. Run when user presses Enter OR button
user_input = None
submit_button = None

# Input box
df = functions.read_data("../data/ecommerce-website-logs.csv")
user_input = st.multiselect(
    "Please select at least two countries you would like the Carbon Emissions for below:",
    df['country'].unique())
submit_button = st.button("Get Carbon Emissions")

if submit_button:
    if len(user_input) < 2:
        st.error("Please select at least two countries you would like the Carbon Emissions for above.")
    else:
        df = functions.process_data("../data/ecommerce-website-logs.csv", user_input)
        bot_response = []
        figure = functions.plot_country(df)
        for country in user_input:
            row = df[df['country'] == country]
            gco2e = row.iloc[0]['gco2e']
            bot_response.append(f"The Carbon Emissions for {country} is {gco2e:.2f} g/m^3.")

        final_bot_response = " ".join(bot_response)

        st.session_state.history.append({
            "user": f"Countries: {', '.join(user_input)}",
            "bot": final_bot_response,
        })

        st.write("Carbon Emissions in CO2 g/m^3 by Country")
        st.bar_chart(df.set_index("country"))

# 3. Display the chat history
for i, chat in enumerate(st.session_state.history):
    message(chat["user"], is_user=True, key=f"user_{i}")
    message(chat["bot"], key=f"bot_{i}")