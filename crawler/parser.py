import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


class Parser():
    '''
    Get image source urls from a web page
    '''

    def __init__(self, url, depth=1):
        self.url = url
        self.depth = depth
        self.host = self.get_host_from_url()
        self.base_url = self.get_base_url()
        self.parsed_urls = []
        self.results = []
        self.parser([url])

    def is_absolute_url(self, url):
        '''
        Check if url is absolute or not
        '''
        return bool(urlparse(url).netloc)

    def get_img_src_from_soup(self, soup):
        '''
        Return all image sources from the parsed html soup
        if url is not absolute then append base_url to it.
        '''
        all_img = soup.findAll('img', src=True)
        images = []
        for img in all_img:
            if self.is_absolute_url(img['src']):
                images.append(img['src'])
                continue
            images.append(urljoin(self.base_url, img['src']))
        return images

    def get_a_href_from_soup(self, soup):
        '''
        Return all anchor tag hrefs from the parsed html soup
        if url is not absolute then append base_url to it.
        '''
        all_a = soup.findAll('a', href=True)
        a_hrefs = []
        for a in all_a:
            href = a['href'].split('#')[0].rstrip('/')
            if self.is_absolute_url(href):
                if self.host in href:
                    a_hrefs.append(href)
                    continue
                else:
                    continue
            a_hrefs.append(urljoin(self.base_url, href))
        return a_hrefs

    def get_host_from_url(self):
        parsed_url = urlparse(self.url)
        return parsed_url.netloc

    def get_base_url(self):
        parsed_url = urlparse(self.url)
        return parsed_url.scheme + '://' + parsed_url.netloc

    def parser(self, urls):
        images = []
        a_hrefs = []
        for url in urls:
            if url in self.parsed_urls:
                continue
            print(url)
            try:
                response = requests.get(url)
            except:
                self.parsed_urls.append(url)
                continue
            if response.status_code != 200:
                continue
            self.parsed_urls.append(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            images.append(
                {'url': url, 'images': self.get_img_src_from_soup(soup)})
            a_hrefs.extend(self.get_a_href_from_soup(soup))
        self.results.extend(images)
        if self.depth != 0:
            self.depth -= 1
            self.parser(a_hrefs)
