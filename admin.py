import pandas as pd
from src.data_extraction.scrapping_utils import WebScrap
RED_BUS_URL = "https://www.redbus.in/online-booking/rtc-directory"
scrap_obj = WebScrap(RED_BUS_URL)
scrap_obj.extract_all_rtc_operators()
print(scrap_obj.bus_list)
