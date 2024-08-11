import streamlit as st
import pandas as pd
from src.data_layer.data_access import RedBusData
from src.redbus_constants import DBNAME
data_obj = RedBusData()
data_obj.create_connection(DBNAME)
res=data_obj.fetch_data("select Text from redbusdata2")
res = [item[0] for item in res]
df = pd.read_excel('rtc_list.xlsx')
bus_routes = df['Text']
st.title("RedBus")
option = st.multiselect(
    'Choose youre Bus Route:',
    res
)

if option :
    if len(option) ==1:
        param = f"('{option[0]}')"
    else:
        param = tuple(option)
    query  = f"select * from live_redbus_data where route_name in {param} "
    print(query)
    data = data_obj.fetch_data(query)
    st.dataframe(data)
st.write(f'You selected: {option}')

