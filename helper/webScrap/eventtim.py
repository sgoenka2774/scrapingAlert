import re
from connect import connection
from bs4 import BeautifulSoup

def filterNumber(num):
    return int(num)

def websiteEventim(tag):
    page_num = 0
    response = connection(f"https://www.eventim.de/search/?affiliate=EVE&searchterm={tag}")
    print(response['text'])
    if response['status_code'] == 200:
        soup = BeautifulSoup(response['text'], 'html_parser')
        count_in_text = soup.find('div',{'aria-live': 'assertive'}).text
        number_of_ticket = re.findall(r'\d+',count_in_text)[0]




websiteEventim('ticket')
