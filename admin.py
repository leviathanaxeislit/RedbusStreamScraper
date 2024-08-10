import pandas as pd
from src.data_extraction.scrapping_utils import WebScrap
from src.redbus_constants import RED_BUS_URL
scrap_obj = WebScrap(RED_BUS_URL)
scrap_obj.extract_all_rtc_operators()
df = pd.DataFrame(scrap_obj.bus_list)
df.to_excel("rtc_list.xlsx")
print(scrap_obj.bus_list)
