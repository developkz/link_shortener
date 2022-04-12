# Link Shortener

The script receives a short link through the Bitly API. And also get the number of clicks for links created by the user earlier.

## Bitli API Token

This stript can't work witout Bitlink access token. To get Bitkink use the following instructions [Click here](https://support.bitly.com/hc/en-us/articles/230647907-How-do-I-generate-an-OAuth-access-token-for-the-Bitly-API-)

## Environment setup

Copy or clone this repository to your local machine.

Rename `.env.sample` in to `.env`.
Replase `<Your bitlink token>`to your Bitlink token.

Should be something similar to:
```BITLINK_TOKEN=Bearer 23123hoy48124ydqs7dglqs7dgbdoqbwd78```

To activate environment run command:

```sh
source link_shortener_venv/bin/activate
```

## Documentation

Run script. Paste your link and press Enter. You shoud see in command line:

Script answer if this link is not Bitlink:

```sh
Paste bitlink/url here: https://google.com
Bitlink created: https://bit.ly/3DCyocP
```

Script answer if Bitlink is already created:

```sh
Paste bitlink/url here: https://bit.ly/3DCyocP
Clicks count: 3
```
