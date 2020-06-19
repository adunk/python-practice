import json
from urllib import request


def main():
    try:
        # The json.load() method will convert the request response into a dictionary object
        data = json.load(request.urlopen('https://ipinfo.io/json'))
        # Reminder that the ** unpacking will unpack the dictionary into separate properties by key / value
        print('You are near: {city}, {region}, {country}'.format(**data))
        print('Lat/Lng: {}E'.format(data['loc'].replace(',', 'N, ')))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
