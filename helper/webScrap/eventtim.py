import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def filterNumber(number):
    num = ''
    for n in number:
        try:
            if int(n) >= 0:
                num = num + str(n)
        except:
            continue
    return int(num)


def eventtim(tag):
    driver = webdriver.Chrome()
    driver.get(f"https://www.eventim.de/search/?affiliate=EVE&searchterm={tag}")
    time.sleep(5)
    html = driver.page_source
    script = '''return document.querySelectorAll("div[class='search-result-content']")[0].outerText'''
    text = driver.execute_script(script)
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    list_ticket_name = soup.find_all("div", class_="event-listing-city theme-text-color")
    new_ticket_name = []
    for n in list_ticket_name:
        new_ticket_name.append(n.text)
    number = filterNumber(text)

    return [number, new_ticket_name]

