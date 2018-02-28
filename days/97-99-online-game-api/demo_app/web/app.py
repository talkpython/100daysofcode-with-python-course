import flask
from game_logic import game_decider, game_service
from views import game_api, home

app = flask.Flask(__name__)


def main():
    build_starter_data()
    build_views()
    run_web_app()


def build_views():
    game_api.build_views(app)
    home.build_views(app)


def build_starter_data():
    roll_names = game_decider.all_roll_names()
    game_service.init_rolls(roll_names)

    computer = game_service.find_player('computer')
    if not computer:
        game_service.create_player('computer')


def run_web_app():
    app.run(debug=True)


if __name__ == '__main__':
    main()
