import re
import shutil

import bs4
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# This was installed using homebrew to get around macos permission issues
CHROME_PATH = '/usr/local/bin/chromedriver'


def main():
    # params = '?order=sol&per_page=50&page=0&mission=msl&af=FHAZ_RIGHT_A%7CFHAZ_LEFT_A%7CFHAZ_RIGHT_B%7CFHAZ_LEFT_B%2C'
    # clean = urllib.parse.parse_qs(params)

    url = 'https://mars.nasa.gov/msl/multimedia/raw-images/?order=sol&per_page=50&page=0&mission=msl&fbl=2794'
    # params = {'order': 'sol', 'per_page': 50, 'page': 0, 'mission': 'msl', 'fbl=': 2794}

    browser = webdriver.Chrome(CHROME_PATH)
    browser.get(url)
    WebDriverWait(browser, 10).until(lambda x: x.find_elements_by_class_name('raw_image_gallery'))

    soup = bs4.BeautifulSoup(browser.page_source, 'html.parser')

    gallery = soup.find('div', attrs={'class': 'raw_image_gallery'})
    images = [re.sub('-thm', '', img['src']) for img in gallery.find_all('img')]

    for image in images:
        response = requests.get(image, stream=True)
        if response.status_code == 200:
            # Split the image path by / and take the last element, which is the file name
            name = image.split('/').pop()
            with open('./images/' + name, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)

    browser.quit()


if __name__ == '__main__':
    main()
