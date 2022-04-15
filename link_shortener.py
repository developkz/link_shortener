import os
import urllib.request
import urllib.error

from pathlib import Path
from urllib.parse import urlparse

import requests

from dotenv import load_dotenv


def check_url_accessibility(url: str) -> bool:
    if urllib.request.urlopen(url).getcode() == 200:
        return True
    else:
        return


def is_bitlink(token: str, url: str) -> str:
    '''The function returns the number of clicks on the bitlink.
    If there is no such bitlink, the bitlink will be returned.'''

    headers = {
        'Authorization': f'Bearer {token}',
    }

    api_link = 'https://api-ssl.bitly.com/v4/bitlinks/{}'
    request_link = api_link.format(urlparse(url).netloc + urlparse(url).path)
    bitly_response = requests.get(request_link, headers=headers)
    if bitly_response.ok:
        return True
    else:
        return


def get_click_count(token: str, url: str) -> int:
    '''Function returns click count all time for bitlink'''

    headers = {
        'Authorization': f'Bearer {token}',
    }

    api_link = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'
    request_link = api_link.format(urlparse(url).netloc + urlparse(url).path)
    bitly_response = requests.get(request_link, headers=headers)
    bitly_response.raise_for_status()
    return bitly_response.json()['total_clicks']


def get_shorten_link(token: str, url: str) -> str:
    '''Function returns shortern link'''

    headers = {
        'Authorization': f'Bearer {token}',
    }
    data = {'long_url': url}
    bitly_response = requests.post(
            'https://api-ssl.bitly.com/v4/bitlinks',
            headers=headers,
            json=data
    )
    bitly_response.raise_for_status()
    return bitly_response.json()['link']


if __name__ == '__main__':

    env_path = Path('.') / '.env'
    load_dotenv(env_path)
    bitlink_token = os.getenv('BITLINK_TOKEN')

    user_input = input(f'Paste bitlink/url here: ').strip()
    try:
        if check_url_accessibility(url=user_input):
            try:
                if is_bitlink(token=bitlink_token, url=user_input):
                    print(f'Clicks Count: {get_click_count(token=bitlink_token, url=user_input)}')
                else:
                    print(f'Shorten Link: {get_shorten_link(token=bitlink_token, url=user_input)}')
            except:
                raise requests.exceptions.HTTPError('Link is invalid. Link format is https://google.com')
    except:
        raise urllib.error.URLError('Website is down')
