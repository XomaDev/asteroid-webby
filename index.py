from flask import Flask, request

import chocolateo

app = Flask(__name__)


@app.route('/')
def home():
    return 'Asteroid is working! :)'


@app.route('/api/answer')
def api():
    text = request.args.get("text")
    result = chocolateo.web_scrape(text)
    return '{ "answer":"' + result[0] + '", "source":"' + result[1] + '"}'
