import json
from urllib import request


def main():
    try:
        data = json.load(request.urlopen('https://ipinfo.io/json'))
    except Exception as e:
        print(e)
    else:
        print('You are near: {city}, {region}, {country}'.format(**data))
        print('Lat/Lng: {}E'.format(data['loc'].replace(',', 'N, ')))


if __name__ == '__main__':
    main()
