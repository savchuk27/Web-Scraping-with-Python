import requests
import csv
from multiprocessing import Pool

def get_html(url):
    r = requests.get(url)
    return r.text

def write_csv(data):
    with open('websites.csv','a') as f:
        order = ['name','url','description','traffic','percent']
        writer = csv.DictWriter(f,fieldnames=order)
        writer.writerow(data)



def get_page_data(text):
    # for i in range(0, 6428):
    #     url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'.format(str(i))
    #     response = get_html(url)
        data = text.strip().split('\n')[1:]

        for row in data:
            columns = row.strip().split('\t')
            name = columns[0]
            url = columns[1]
            description = columns[2]
            traffic = columns[3]
            percent = columns[4]

            data = {'name': name,
                    'url': url,
                    'description': description,
                    'traffic': traffic,
                    'percent': percent}
            write_csv(data)

def make_all(url):
    text = get_html(url)
    get_page_data(text)

def main():

    url = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'
    urls = [url.format(str(i)) for i in range(1,6321)]
    with Pool(20) as p:
        p.map(make_all, urls)

if __name__ == '__main__':
    main()