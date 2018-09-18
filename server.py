from flask import Flask, redirect
import wikinews


app = Flask(__name__)

@app.route('/')
def home():
    url = wikinews.get_random_news_link()

    return redirect(url)
