import os,logging
import pandas as pd
from src.data_extraction.scrapping_utils import WebScrap
from src.data_layer.data_access import RedBusData
from src.redbus_constants import RED_BUS_URL , DB_SCHEMA , DBNAME ,RED_BUS_INFO ,RED_BUS_MAIN_TABLE
table_name = "redbusdata2"
scrap_obj = WebScrap(RED_BUS_URL)
db_obj =RedBusData()

scrap_obj.extract_all_rtc_operators()         #extracting bus infromations
df = pd.DataFrame(scrap_obj.bus_list)
df.to_excel("rtc_list.xlsx")
print(scrap_obj.bus_list)
for operator in scrap_obj.bus_list:
    scrap_obj.scrape_all_pages(operator)
all_bus_df = pd.DataFrame(scrap_obj.all_bus_details)
all_bus_df.to_excel("redbus_allbus_details.xlsx")
if os.path.isfile("redbus_allbus_details.xlsx"):
    logging.info("Data scrapped and file created")

db_obj.create_connection(DBNAME)   #create table and insert to db
df=pd.read_excel("redbus_allbus_details.xlsx")
df.columns = df.columns.str.lower()
df['price'] = df['price'].replace({'INR ': ''}, regex=True)
df['seats_available'] = df['seats_available'].replace({' Seats available': ''}, regex=True)
db_obj.create_table_if_not_exists(RED_BUS_MAIN_TABLE , RED_BUS_INFO )
for i in range(df.shape[0]):
        col=list(df.iloc[i])
        col[7] = float(col[7])
        db_obj.insert_data(RED_BUS_MAIN_TABLE , list(df.columns) , tuple(col))
    

