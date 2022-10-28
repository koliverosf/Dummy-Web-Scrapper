import requests

from bs4 import BeautifulSoup


def get_hyperlink(letter, link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    names = []
    links = soup.findAll('a')
    for a_link in links:
        if a_link.text.startswith(letter) and len(a_link.text) > 1:
            if 'topics' in a_link.get('href') or 'entity' in a_link.get('href'):
                names.append(a_link.text)
    r.close()
    return names


def main():
    letter = 'S'
    link = input()

    print(get_hyperlink(letter, link))


if __name__ == "__main__":
    main()
