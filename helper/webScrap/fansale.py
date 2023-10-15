import re
from bs4 import BeautifulSoup
from .connect import connection

def filterNumber(number):
    num = ''
    for n in number:
        try:
            if int(n) >= 0:
                num = num + str(n)
        except:
            continue
    return int(num)

def websiteFansale(tag):
    url = f'https://www.fansale.at/fansale/events.htm?searchText={tag}'
    new_ticket_name = []
    try:
        response = connection(url)
    except TimeoutError:
        print('timeout')

    if response['status_code'] == 200:
        soup = BeautifulSoup(response['text'], "html.parser")
        list_ticket_name = soup.find_all("h3", class_="EntryDescription-Header")
        count_in_text = soup.find_all("span", class_="RegularRunningText u-nowrap")[0].text
        number_of_ticket = re.findall(r'-?\d+(?:,\d{3})*(?:\.\d+)?',count_in_text)[0]
    page_num = filterNumber(number_of_ticket)
    for n in list_ticket_name:
        new_ticket_name.append(n.text)
    return [page_num, new_ticket_name]

