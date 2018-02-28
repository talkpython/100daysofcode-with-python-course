import flask

app = flask.Flask(__name__)


def main():
    app.run(debug=True)


@app.route('/')
def index():
    return "Hello world!!!"


@app.route('/api/test', methods=['GET'])
def api_test():
    data = {
        'name': 'Michael',
        'day': 97
    }
    return flask.jsonify(data)


@app.errorhandler(404)
def not_found(_):
    return "The page was not found."


if __name__ == '__main__':
    main()
