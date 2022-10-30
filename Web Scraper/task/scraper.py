import string
import os
import requests

from bs4 import BeautifulSoup


def write_in_file(name_file, url, folder):
    file = open(os.path.join(folder, name_file + '.txt'), 'w', encoding='utf-8')
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    text = soup.findAll('div', {'class': 'c-article-body main-content'})[0].text
    file.write(text)
    file.close()
    return 'Success'


def retrieve_information(articles_type, link, folder):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    statuses = []
    articles = soup.findAll('article')
    for article in articles:
        if 'articles' in str(article.findAll('a')[0].attrs) and \
                article.findAll('span', {'class': 'c-meta__type'})[0].text == articles_type:
            url = 'https://www.nature.com{0}'.format(article.findAll('a')[0].attrs['href'])
            title = article.findAll('h3')[0].text.translate(str.maketrans('', '', string.punctuation + '\n')).replace(
                ' ', '_')
            status = write_in_file(title, url, folder)
            statuses.append(status)
    r.close()
    return statuses


def scrap(n_pages, articles_type, url):
    statuses = {}
    for n in range(1, int(n_pages) + 1):
        folder = 'Page_' + str(n)
        if not os.path.exists(folder):
            os.mkdir(folder)
        statuses[n] = retrieve_information(articles_type, url + '&page=' + str(n), folder)

    return statuses


def main():
    n_pages = input()
    articles_type = input()
    url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020'
    print(scrap(n_pages, articles_type, url))


if __name__ == "__main__":
    main()
