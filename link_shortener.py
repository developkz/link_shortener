import os

from pathlib import Path
from urllib.parse import urlparse

import requests


def check_url(url: str) -> str:
    '''The function returns the number of clicks on the bitlink.
    If there is no such bitlink, the bitlink will be returned.'''

    headers = {
        'Authorization': bitlink_token,
    }

    api_link = 'https://api-ssl.bitly.com/v4/bitlinks/{}'
    request_link = api_link.format(urlparse(url).netloc + urlparse(url).path)
    bitly_response = requests.get(request_link, headers=headers)


    if bitly_response.ok:
        return f'Clicks count: {get_click_count(bitlink_token, url)}'
    else:
        return f'Bitlink created: {get_shorten_link(bitlink_token, url)}'


def get_click_count(token: str, url: str) -> int:
    '''Function returns click count all time for bitlink'''

    headers = {
        'Authorization': token,
    }

    api_link = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'
    request_link = api_link.format(urlparse(url).netloc + urlparse(url).path)
    bitly_response = requests.get(request_link, headers=headers)
    bitly_response.raise_for_status()
    return bitly_response.json()['total_clicks']


def get_shorten_link(token: str, url: str) -> str:
    '''Function returns shortern link'''

    headers = {
        'Authorization': token,
    }
    data = {'long_url': url}
    try:
        bitly_response = requests.post(
            'https://api-ssl.bitly.com/v4/bitlinks',
            headers=headers,
            json=data
            )
        bitly_response.raise_for_status()
        return bitly_response.json()['link']
    except requests.exceptions.HTTPError:
        pass


if __name__ == '__main__':

    env_path = Path('.') / '.env'
    bitlink_token = os.getenv('BITLINK_TOKEN')

    print(check_url(url=input(f'Paste bitlink/url here: ').strip()))
