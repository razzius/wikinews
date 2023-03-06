import random
import datetime
import requests
import webbrowser


def get_wikipedia_news_page_title():
    date = datetime.date.today()

    date_string = date.strftime('%Y_%B_%-d')

    return f'Portal:Current_events/{date_string}'


def get_news_data():
    url = f'https://en.wikipedia.org/w/api.php?action=parse&page={get_wikipedia_news_page_title()}&format=json'

    response = requests.get(url)

    return response.json()


def get_news_content():
    return get_news_data()['parse']['text']['*']


def get_random_news_link():
    return random.choice(get_news_data()['parse']['externallinks'])


def main():
    webbrowser.open(get_random_news_link())


if __name__ == '__main__':
    main()
