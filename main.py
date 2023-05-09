import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

from models import WineScraperModel
from tools import create_folder
from notification import general_notify

urls = ["https://ruouvang24h.vn/ruou-vang-tay-ban-nha/page/{}",
        "https://ruouvang24h.vn/ruou-vang-new-zealand/page/{}",
        "https://ruouvang24h.vn/ruou-vang-argentina/page/{}",
        "https://ruouvang24h.vn/ruou-vang-duc/page/{}",
        "https://ruouvang24h.vn/ruou-vang-bo-dao-nha/{}"]
wines = []
wine_infos = pd.DataFrame(
    columns=['appelation', 'producer', 'region', 'country', 'vintage'
             'wine_type', 'grape_variety', 'alcohol_content', 'volume'])
time_out = 3

# Spain Wines

"""Initializes Edge driver"""
edge_options = webdriver.EdgeOptions()
edge_options.add_argument('--headless')
edge_options.add_argument('--no-sandbox')
edge_options.add_argument('--disable-dev-shm-usage')
edge_service = Service(executable_path='edgedriver')

driver = webdriver.Edge(service=edge_service, options=edge_options)
if driver is None:
    general_notify.notify("Create Edge Driver", "failure")
else:
    general_notify.notify("Create Edge Driver", "success")




# 
wineScraperModel = WineScraperModel.WineScraper()
spain_wine_names, spain_wine_urls = wineScraperModel.scrape_wine_cards(urls[0], n=15)
len(spain_wine_names), len(spain_wine_urls)

# 
cols = ['appelation', 'producer', 'region', 'country', 'vintage', 'wine_type', 'grape_variety', 'alcohol_content', 'volume', 'image_filename']
df = pd.DataFrame(columns=cols)
saved_folder = create_folder.create_new_folder("image")
df.head()

# 
# insert values into the dataframe
for i in range(0, len(spain_wine_urls)):
    temp = wineScraperModel.scrape_wine_info(driver, spain_wine_urls[i], spain_wine_names[i], saved_folder)
    if temp[0] != -1:
        df.loc[i] = temp
    time.sleep(5)
    print(f'Finished looking at item {spain_wine_names[i]}, need some sleep\n...\nOk, Back to Work')

# 
create_folder.create_new_folder("wine_data")
df.to_csv('wine_data/spain_wine_data.csv')

# 
df.head()