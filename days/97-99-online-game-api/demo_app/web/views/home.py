import flask


def build_views(app):
    @app.route('/')
    def index():
        return "Hello world!!!"

    @app.errorhandler(404)
    def not_found(_):
        return flask.Response("The page was not found.", status=404)


