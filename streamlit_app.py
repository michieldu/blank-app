import streamlit as st
import pandas as pd
import os

# Function to load existing rankings
def load_rankings():
    if os.path.exists('rankings.csv'):
        return pd.read_csv('rankings.csv')
    return pd.DataFrame(columns=['Username', 'Time (min:sec)'])

# Function to save rankings
def save_ranking(username, time_display):
    df = load_rankings()
    df = df.append({'Username': username, 'Time (min:sec)': time_display}, ignore_index=True)
    df.to_csv('rankings.csv', index=False)

# Initialize Streamlit app
st.title("Timer Application")
username = st.text_input("Enter your username:")

# Load rankings
rankings = load_rankings()
st.write("Current Rankings:")
st.write(rankings)

# The rest of your timer logic...

if st.button("Accept"):
    save_ranking(username, time_display)
    st.success("Time recorded!")

