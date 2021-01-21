import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    r = requests.get(url)
    return r.text


def refind(s):
    # 1,123 total rating
    r = s.split(' ')[0]
    result = r.replace(',', '')
    return result


def write_csv(data):
    with open('plugins.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['url'],
                         data['rating']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[3]
    plugins = popular.find_all('article')

    for plugin in plugins:
        name = plugin.find('h2').text
        url = plugin.find('h2').find('a').get('href')
        r = plugin.find('span',class_= 'rating-count').find('a').text
        rating = refind(r)

        data = {'name': name,
                'url': url,
                'rating' : rating}
        # print(data)
        write_csv(data)
    # return plugins



def main():
    url = 'https://wordpress.org/plugins/'
    print(get_data(get_html(url)))




if __name__ == '__main__':
    main()
