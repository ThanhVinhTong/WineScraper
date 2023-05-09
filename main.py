import pandas as pd
import time

from drivers import EdgeDriver
from models import WineScraperModel
from tools import CreateFolder


urls = ["https://ruouvang24h.vn/ruou-vang-tay-ban-nha/page/{}",
        "https://ruouvang24h.vn/ruou-vang-new-zealand/page/{}",
        "https://ruouvang24h.vn/ruou-vang-argentina/page/{}",
        "https://ruouvang24h.vn/ruou-vang-duc/page/{}",
        "https://ruouvang24h.vn/ruou-vang-bo-dao-nha/{}"]
wines = []
wine_infos = pd.DataFrame(
    columns=['appelation', 'producer', 'region', 'country', 'vintage'
             'wine_type', 'grape_variety', 'alcohol_content', 'volume'])
max_page_number = 50

driver = EdgeDriver.initiate()

# 
wineScraperModel = WineScraperModel.WineScraper()
wine_names, wine_urls = wineScraperModel.scrape_wine_cards(driver, urls[0], n=max_page_number)

# 
cols = ['appelation', 'producer', 'region', 'country', 'vintage', 'wine_type', 'grape_variety', 'alcohol_content', 'volume', 'image_filename']
df = pd.DataFrame(columns=cols)
saved_folder = CreateFolder.create_new_folder("image")

# insert values into the dataframe
for i in range(0, len(wine_urls)):
    temp = wineScraperModel.scrape_wine_info(driver, wine_urls[i], wine_names[i], saved_folder)
    if temp[0] != -1:
        df.loc[i] = temp
    time.sleep(5)
    print(f'Finished looking at item {wine_names[i]}, need some sleep\n...\nOk, Back to Work')

# 
CreateFolder.create_new_folder("wine_data")
df.to_csv('wine_data/wine_data.csv')