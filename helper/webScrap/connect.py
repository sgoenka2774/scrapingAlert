import requests



def connection(url):
    response = None
    '''custom function for requests '''
    # Create a Session object
    session = requests.Session()

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0',
        'Accept-Language': 'en-US,en;q=0.5'
    }

    session.headers.update(headers)
    # Define the URL you want to request
    #url = "https://www.kleinanzeigen.de/s-eintrittskarten-tickets/wanda/k0c231"
    #"https://www.eventim.de/search/?affiliate=EVE&searchterm=ticket"

    # Send the initial request to get cookies
    try:
        response = session.get(url)
    except:
        print('Error while retriving cookies')

    # The cookies are now stored in the session

    # Make subsequent requests, and the cookies will be automatically included
    try:
        response = session.get(url)
    except:
        print('Error while creating session')
    # If the server sets new cookies, the session will automatically update them
    # Close the session when done
    session.close()
    return {'status_code': response.status_code, 'text': response.text}

