import streamlit as st
import datetime
import pandas as pd
from src.redbus_ui.redbus_styles import RedBusInterfaceEnhancement 
from src.data_layer.data_access import RedBusData
from src.redbus_constants import DBNAME , RED_BUS_MAIN_TABLE
ui_obj = RedBusInterfaceEnhancement()
data_obj = RedBusData()
data_obj.create_connection(DBNAME)

#data fetch
route_link =list(data_obj.fetch_data(f"select distinct(route_link) from {RED_BUS_MAIN_TABLE}"))
price_list =list(data_obj.fetch_data(f"select distinct(price) from {RED_BUS_MAIN_TABLE}"))
price_list=[x[0] for x in price_list ]
rating = list(data_obj.fetch_data(f"select distinct(star_rating) from {RED_BUS_MAIN_TABLE}"))
seats = list(data_obj.fetch_data(f"select distinct(seats_available) from {RED_BUS_MAIN_TABLE}"))
routes = list(set(list(map(lambda item:item[0].split(' ')[0] , route_link))))
bus_types = [x[0] for x in list(data_obj.fetch_data(f"select distinct(bustype) from {RED_BUS_MAIN_TABLE}"))]
filtered_data = list(data_obj.fetch_data(f"select * from {RED_BUS_MAIN_TABLE} limit 10"))

def filter_ac(display_data):

    '''
    filter function to filter AC buses 
    '''
    ac_filtered_data = []
    ac_filter = ["non" , "NON" ,"Non"]
    for item in display_data:
      element =item[4].split(' ')[0]
      if element not in ac_filter:
                    ac_filtered_data.append(item)
    print("filter",len(ac_filtered_data))
    return ac_filtered_data


def filter_seater(display_data):
    '''
    filter function to filter seater types 
    '''
    seater_filtered_data = []
    seater_filter = ["seater" , "Seater" , "SEATER"]
    for item in display_data:
      for element in item[4].split(' '):
        if element  in seater_filter:
                    seater_filtered_data.append(item)
    return seater_filtered_data

# Streamlit App
st.set_page_config(page_title="RedBus Dynamic Filter", layout="wide")

# App Bar
st.markdown("<h1 style='text-align: center; color: red;'>RedBus</h1>", unsafe_allow_html=True)

# Sidebar filters
st.sidebar.header("Filter Options")
#selected_bus_operator = st.sidebar.multiselect("Bus Operator", bus_data['Bus Operator'].unique())
source = st.sidebar.selectbox("Going from" , routes)
destination = st.sidebar.selectbox("Going To" ,  list(filter(lambda element:element not in  source,routes)))
selected_price_range = st.sidebar.slider("Price Range",min_value = int(min(price_list)) , max_value=int(max(price_list)) ,step =100)
selected_ratings = st.sidebar.slider("Ratings",1,5,1 )
selected_seats_available = st.sidebar.slider("Seats Available", 1,int(max(seats[0])),1 )
st.sidebar.write("Bus Types")
ac = st.sidebar.checkbox("AC")
seater= st.sidebar.checkbox("Seater")
route = f"{source} to {destination}"

primary_query = f"select * from {RED_BUS_MAIN_TABLE} where route_link ='{route}'"
primary_data = data_obj.fetch_data(primary_query)
primary_data = list(primary_data) if primary_data else []

data_query = f"select * from {RED_BUS_MAIN_TABLE} where route_link ='{route}' and price <= {selected_price_range} and star_rating <= {selected_ratings} and seats_available >= {selected_seats_available}"

filtered_data=data_obj.fetch_data(data_query)
filtered_data = list(filtered_data) if filtered_data else []
if primary_data:
    display_data = filtered_data if filtered_data else primary_data
else:
    display_data =[]
if ac and display_data :
    display_data = filter_ac(display_data)
if seater and display_data :
    display_data = filter_seater(display_data)
    
st.subheader("Available Buses")
st.write(f"Total buses found: {len(display_data)}")

for bus in display_data:
    st.markdown(ui_obj.create_card(bus), unsafe_allow_html=True)

# Footer
st.markdown("<h3 style='text-align: center;'>Happy Journey!</h3>", unsafe_allow_html=True)
