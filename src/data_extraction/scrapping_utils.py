import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


class WebScrap:
    def __init__(self , source_link):
        self.source_link = source_link
        self.all_bus_details = []



    def initialize_driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver

    def load_page(self,driver, url):
        driver.get(url)
        time.sleep(5)      

    def extract_all_rtc_operators(self):
        '''
        function to extract all rtc operators
        '''
        driver = self.initialize_driver()
        self.load_page(driver , self.source_link)

        # Find elements by class name 'D113_ul_rtc'
        content_elements = driver.find_elements(By.CLASS_NAME, 'D113_ul_rtc')
        bus_routes = {}
        self.bus_list = []
        # Loop through each 'D113_ul_rtc' element
        for content in content_elements:
            
            # Find all 'li' elements within the 'D113_ul_rtc' element
            list_items = content.find_elements(By.TAG_NAME, 'li')
            
            for item in list_items:
                # Try to find an 'a' tag within the 'li' element
                try:
                    link = item.find_element(By.TAG_NAME, 'a')
                    link_text = link.text
                    link_href = link.get_attribute('href')
                    self.bus_list.append({"Text" : link_text , "Link" : link_href})
                    #print(f'Text: {link_text}, Link: {link_href}')
                except Exception as e:
                    # Print the strong text if 'a' tag is not found (e.g., region name)
                    strong_text = item.find_element(By.TAG_NAME, 'strong').text
                    print(f'Region: {strong_text}')
        if self.bus_list:
            return True

      
      
                

    
    