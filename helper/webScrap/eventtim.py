import re
from connect import connection
from bs4 import BeautifulSoup

def filterNumber(num):
    return int(num)

def websiteEventim(tag):
    page_num = 0
    response = connection(f"https://www.eventim.de/search/?affiliate=EVE&searchterm={tag}&tab=1")
    if response['status_code'] == 200:
        soup = BeautifulSoup(response['text'], 'html.parser')
        count_in_text = soup.find_all(lambda tag: tag.name == 'div' and tag.get('aria-live') == 'assertive')

        print(count_in_text)
        #number_of_ticket = re.findall(r'\d+',count_in_text)[0]
        #page_num = filterNumber(number_of_ticket)

    #print(page_num)




websiteEventim('ticket')
