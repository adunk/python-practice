import re
import subprocess

import requests

# https://developers.google.com/maps/documentation/geolocation/intro
# https://blog.ouseful.info/2016/01/27/looking-up-the-physical-location-of-your-wifi-router/
# Potentially https://github.com/ohwada/geo_wifi/blob/master/geo_wifi.py

API_URL = 'https://www.googleapis.com/geolocation/v1/geolocate?key='
API_KEY = 'AIzaSyDyKn1YEW2N9HgTLc9_HyghIbvqr8zufSA'

payload = {'considerIp': 'true'}

try:
    # Runs a command to find any networks the computer knows about
    cmdout = subprocess.check_output(["/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport", "-s"])
    cmdout = cmdout.decode("utf-8")

    # Splits output by line but leaves a lot of spaces
    ls = cmdout.split("\n")
    # Create a new list starting from position 1 (effectively removing the first row as a header)
    ls = ls[1:]

    addresses = []

    # Go through each line while also stripping out all the white spaces
    for line in [x.strip() for x in ls if x.strip() != '']:
        # Our crazy re to find the right match of addr, signal, and channel broken down by groups
        match = re.search(r'((?:[0-9a-fA-F]:?){12})\s(-[0-9]+)\s\s([\w]+)', line)
        if match:
            addresses.append({'addr': match.group(1), 'signal': match.group(2), 'channel': match.group(3)})

    if not addresses:
        raise Exception('Could not retrieve WiFi Access Points...')
except Exception as e:
    print(e)
else:
    print('Using {0} WiFi Access Point{1}...'.format(len(addresses), 's' if (len(addresses) > 1) else ''))
    wifi_list = []
    for item in addresses:
        try:
            int(item['signal'])
            is_dig = True
        except ValueError:
            is_dig = False
        if is_dig:
            wifi_list.append({
                'macAddress': item['addr'],
                'signalStrength': item['signal'],
                'channel': item['channel'],
            })
    payload['wifiAccessPoints'] = wifi_list

# Make request via Google Maps API
try:
    response = requests.post(API_URL + API_KEY, json=payload)
    data = response.json()
    if 'error' in data.keys():
        raise requests.RequestException('Error {0}: {1}'.format(data['error']['code'], data['error']['message']))
except Exception as e:
    print(e)
else:
    lat = data['location']['lat']
    lng = data['location']['lng']
    accuracy = data['accuracy']
    print('You are within {0}m of {1}N {2}E'.format(accuracy, lat, lng))
