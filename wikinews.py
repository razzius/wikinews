import random
import datetime
import requests
import webbrowser


def get_wikipedia_news_page_title():
    date = datetime.date(2018, 9, 10)

    date_string = date.strftime('%Y %B %d')

    return f'Portal:Current%20events/{date_string}'


def get_news_content():
    url = f'https://en.wikipedia.org/w/api.php?action=parse&page={get_wikipedia_news_page_title()}&format=json'

    print(url)
    response = requests.get(url)

    data = response.json()

    return data['parse']['text']['*']


def main():
    webbrowser.open(get_random_news_link())


if __name__ == '__main__':
    main()
