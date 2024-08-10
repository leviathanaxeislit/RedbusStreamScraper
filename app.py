import streamlit as st
from src.data_extraction.scrapping_utils import WebScrap
from admin import RED_BUS_URL
scrap_obj = WebScrap(RED_BUS_URL)
scrap_obj.extract_all_rtc_operators()
bus_routes  = [item.get("Text") for item in scrap_obj.bus_list]
st.title("RedBus")
option = st.selectbox(
    'Choose youre Bus Route:',
    bus_routes
)


st.write(f'You selected: {option}')

