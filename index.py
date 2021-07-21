from json import JSONEncoder

from flask import Flask, request

import chocolateo

app = Flask(__name__)


@app.route('/')
def home():
    return 'Asteroid is working! :)'


@app.route('/api/answer')
def answer():
    result = chocolateo.web_scrape(request.args.get("text"))

    return app.response_class(
        response=JSONEncoder().encode({
            "answer": result[0],
            "source": result[1]
        }),
        status=200,
        mimetype='application/json'
    )
