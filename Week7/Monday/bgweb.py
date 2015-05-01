from histogram import Histogram
from bs4 import BeautifulSoup
import requests


def main():
    url = "http://register.start.bg/"
    page_source = requests.get(url)
    soup = BeautifulSoup(page_source.text)
    histogram = Histogram()

    all_urls = []

    for link in soup.find_all('a'):
        all_urls.append(link.get('href'))

    link_urls = []

    for url in all_urls:
        if url is not None and "link.php?id=" in url:
            full_url = 'http://register.start.bg/' + url
            link_urls.append(full_url)

    server_list = []

    for url in link_urls:
        try:
            r = requests.head(url, timeout=3, allow_redirects=True)
            server_list.append(r.headers["Server"])
        except:
            pass

    for server in server_list:
        if 'Apache' in server:
            histogram.add('Apache')
        elif 'IIS' in server:
            histogram.add('IIS')
        elif 'nginx' in server:
            histogram.add('nginx')
        elif 'lighttpd' in server:
            histogram.add('lighttpd')

    print(histogram.get_dict())

if __name__ == '__main__':
    main()
