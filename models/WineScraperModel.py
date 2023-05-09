from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm

import requests
import time

from tools import save_image_tool
from tools import map_info


class WineScraper:
    def __init__(self, driver):
        self.driver = driver

    def scrape_wine_cards(self, wine_url, n):
        wine_urls = []
        wine_names = []
        for page_number in tqdm(range(1, n)):
            self.driver.get(wine_url.format(page_number))
            wine_cards = self.driver.find_elements(By.CLASS_NAME, "product-meta")
            for card in wine_cards:
                card = card.find_element(By.CLASS_NAME, "pro-link.pro-review")
                wine_urls.append(card.get_attribute('href'))
                wine_names.append(card.get_attribute("title"))
        return wine_names, wine_urls

    def scrape_wine_info(self, wine_url, wine_name, saved_folder):
        self.driver.get(wine_url)
        time.sleep(1)
        cols = self.driver.find_elements(By.CLASS_NAME, 'col-xs-6.col-sm-6.left')
        infos = self.driver.find_elements(By.CLASS_NAME, 'col-xs-6.col-sm-6.border-left.right.min-height-30')
        if len(cols)-1 != 7:
            return [-1]
        else:
            wine_name = wine_name.lower()
            country, region, producer, wine_type, alcohol_content, volume, grape_variety = map_info.find_info(cols, infos)
            vintage = 1980
            image_href = self.driver.find_element(By.CLASS_NAME, 'thumbnail-product-template').find_element(By.TAG_NAME, 'img').get_attribute('src')
            image_path = save_image_tool.save_image_to_folder(image_href, saved_folder)
            return [wine_name, producer, region, country, vintage, wine_type, grape_variety, alcohol_content, volume, image_path]