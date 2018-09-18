from flask import Flask, redirect
import wikinews


app = Flask(__name__)

@app.route('/')
def home():
    return wikinews.get_news_content()
