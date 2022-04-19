import os

from pathlib import Path
from urllib.parse import urlparse

import requests

from dotenv import load_dotenv


def check_url_accessibility(url: str) -> bool:
    '''Function checks url for avaliblity'''
    if requests.get(url).raise_for_status:
        return True



def is_bitlink(token: str, url: str) -> str:
    '''The function returns the number of clicks on the bitlink.
    If there is no such bitlink, the bitlink will be returned.'''

    api_link = 'https://api-ssl.bitly.com/v4/bitlinks/{}'
    request_link = api_link.format(urlparse(url).netloc + urlparse(url).path)
    bitly_response = requests.get(request_link, headers=token)
    return bitly_response.ok


def get_click_count(token: str, url: str) -> int:
    '''Function returns click count all time for bitlink'''

    api_link = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'
    request_link = api_link.format(urlparse(url).netloc + urlparse(url).path)
    bitly_response = requests.get(request_link, headers=token)
    bitly_response.raise_for_status()
    return bitly_response.json()['total_clicks']


def get_shorten_link(token: str, url: str) -> str:
    '''Function returns shortern link'''

    data = {'long_url': url}
    bitly_response = requests.post(
            'https://api-ssl.bitly.com/v4/bitlinks',
            headers=token,
            json=data
    )
    bitly_response.raise_for_status()
    return bitly_response.json()['link']


if __name__ == '__main__':

    env_path = Path('.') / '.env'
    load_dotenv(env_path)
    bitlink_token = os.getenv('BITLINK_TOKEN')

    user_input = input(f'Paste bitlink/url here: ').strip()
    authorization_header = {'Authorization': f'Bearer {bitlink_token}'}
    try:
        check_url_accessibility(url=user_input)
        if is_bitlink(token=authorization_header, url=user_input):
                print(f'Clicks Count: {get_click_count(token=authorization_header, url=user_input)}')
        else:
                print(f'Shorten Link: {get_shorten_link(token=authorization_header, url=user_input)}')
    except requests.exceptions.ConnectionError:
        print('ConnectionError: can\'t connect to server.')
    except requests.exceptions.HTTPError:
        print('HTTPError: Bad request, or link format. Link format is: https://google.com')
