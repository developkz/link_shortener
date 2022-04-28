# Link Shortener

The script receives a short link through the Bit-ly API. And also get the number of clicks for links created by the user earlier.

## Bitli API Token

This script can't work without Bit-link access token. To get Bit-link use the following instructions [Click here](https://support.bitly.com/hc/en-us/articles/230647907-How-do-I-generate-an-OAuth-access-token-for-the-Bitly-API-)

## Environment setup

Copy or clone this repository to your local machine.

Rename `.env.sample` in to `.env`.
Replace `<Your bitlink token>`to your Bit-link token.

Should be something similar to:
```BITLINK_TOKEN=23123hoy48124ydqs7dglqs7dgbdoqbwd78```

Create environment inside project folder, run command:

```sh
python3 -m venv env
```

To activate environment run command:

```sh
source env/bin/activate
```

## Documentation

Run script. 
```shell
python3 link_shortener.py YOUR_LINK
#Bitlink created: https://bit.ly/3DCyocP
```

Script answer if Bit-link is already created:

```shell
python3 link_shortener.py YOUR_LINK
#Clicks Count: 3
```