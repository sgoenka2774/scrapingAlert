import re
import requests
from bs4 import BeautifulSoup

def filterNumber(number):
    num = ''
    print(str(number).split('.'))
    for n in str(number).split('.'):
        num = num+n
    print(num)
    return round(int(num)/30)

def websiteWill(tag):
    new_ticket_name = []
    number_of_ticket = 0
    response = 'a'
    last_response = 'a'
    url = f'https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/tickets-gutscheine-6700?sfId=a1a0c9c8-8c17-4a3c-bc5f-2bdf3e9c6295&rows=30&isNavigation=true&keyword={tag}'

    try:
        response = requests.get(url, timeout=5)

    except TimeoutError:
        print('Timeout')


    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        cout_in_text = soup.find(id="result-list-title").text
        number_of_ticket = re.findall(r'-?\d+(?:,\d{3})*(?:\.\d+)?',cout_in_text)[0]
    page_num = filterNumber(number_of_ticket)
    url_last_page = f'&page={page_num}&adSeparatorSeen=false'

    try:
        print(url+url_last_page)
        last_response = requests.get(url+url_last_page, timeout=5)
    except TimeoutError:
        print('timeout')
    if last_response.status_code == 200:
        list_soup = BeautifulSoup(last_response.text, 'html.parser')
        for n in list_soup.findAll(class_= "Text-sc-10o2fdq-0 dphSxt"):
            new_ticket_name.append(n.text)
    print(len(new_ticket_name))
    return [number_of_ticket, new_ticket_name]

print(websiteWill('ticket'))
