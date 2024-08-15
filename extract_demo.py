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