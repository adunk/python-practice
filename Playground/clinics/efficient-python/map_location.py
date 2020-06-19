import bs4

with open('data/locations.xml', 'r') as f:
    xml = bs4.BeautifulSoup(f, 'lxml-xml')
    locations = xml.find_all('location')
    print(len(locations))
