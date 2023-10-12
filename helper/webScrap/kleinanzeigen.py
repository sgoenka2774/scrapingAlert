from bs4 import BeautifulSoup
from connect import connection
import requests


def websiteklein(tag):

    response = connection(
        f"https://www.kleinanzeigen.de/s-eintrittskarten-tickets/{tag}/k0c231")
    print(response['text'])
    if response['status_code'] == 200:
        soup = BeautifulSoup(response['text'], "html.parser")
        print(soup.prettify())


websiteklein("assen")
