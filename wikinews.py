import random
import datetime
import requests
import webbrowser


def get_random_news_link():
    date = datetime.date.today()

    date_string = date.strftime('%Y %B %d')

    page = f'Portal:Current%20events/{date_string}'
    url = f'https://en.wikipedia.org/w/api.php?action=parse&page={page}&format=json'

    response = requests.get(url)

    data = response.json()

    return random.choice(data['parse']['externallinks'])


def main():
    webbrowser.open(get_random_news_link())


if __name__ == '__main__':
    main()
