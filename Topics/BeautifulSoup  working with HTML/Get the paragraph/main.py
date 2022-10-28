import requests

from bs4 import BeautifulSoup


def get_paragraph(word, link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    paragraphs = soup.findAll('p')
    for p in paragraphs:
        if word in p.text:
            return p.text
    r.close()
    return None

def main():
    word = input()
    link = input()

    print(get_paragraph(word, link))


if __name__ == "__main__":
    main()
