import string

import requests

from bs4 import BeautifulSoup

def write_in_file(name_file, url):
    file = open(name_file + '.txt', 'w', encoding='utf-8')
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    text = soup.findAll('div', {'class': 'c-article-body main-content'})[0].text
    file.write(text)
    file.close()
    return 'Success'


def get_hyperlinks(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    statuses = []
    articles = soup.findAll('article')
    for article in articles:
        if 'articles' in str(article.findAll('a')[0].attrs) and article.findAll('span',{'class' : 'c-meta__type'})[0].text == 'News':
            url = 'https://www.nature.com{0}'.format(article.findAll('a')[0].attrs['href'])
            title = article.findAll('h3')[0].text.translate(str.maketrans('', '', string.punctuation + '\n' + '’')).replace(' ', '_')
            status = write_in_file(title, url)
            statuses.append(status)
    r.close()
    return statuses


def main():
    letter = 'S'
    link = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3'

    print(get_hyperlinks(link))


if __name__ == "__main__":
    main()
