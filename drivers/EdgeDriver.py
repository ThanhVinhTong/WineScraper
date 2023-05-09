from selenium import webdriver
from selenium.webdriver.edge.service import Service

from notification import GeneralNotification

"""Initializes Edge driver"""

def initiate():    
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument('--disable-gpu')
    edge_options.add_argument('--headless')
    edge_options.add_argument('--no-sandbox')
    edge_options.add_argument('--disable-dev-shm-usage')
    edge_service = Service(executable_path='edgedriver')

    driver = webdriver.Edge(service=edge_service, options=edge_options)
    if driver is None:
        GeneralNotification.notify("Create Edge Driver", "failure")
    else:
        GeneralNotification.notify("Create Edge Driver", "success")

    return driver