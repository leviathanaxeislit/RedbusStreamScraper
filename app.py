import streamlit as st
import pandas as pd
df = pd.read_excel('rtc_list.xlsx')
bus_routes = df['Text']
st.title("RedBus")
option = st.selectbox(
    'Choose youre Bus Route:',
    bus_routes
)


st.write(f'You selected: {option}')

