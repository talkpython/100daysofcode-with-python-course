import random
import uuid

import flask
from game_logic import game_service
from game_logic.game import GameRound


def build_views(app):
    @app.route('/api/game/users/<user>', methods=['GET'])
    def find_user(user: str):
        player = game_service.find_player(user)
        if not player:
            flask.abort(404)
        return flask.jsonify(player.to_json())

    @app.route('/api/game/users', methods=['PUT'])
    def create_user():
        try:
            if not flask.request.json \
                    or 'user' not in flask.request.json \
                    or not flask.request.json.get('user'):
                raise Exception("Invalid request: no value for user.")

            username = flask.request.json.get('user').strip()
            player = game_service.create_player(username)

            return flask.jsonify(player.to_json())

        except Exception as x:
            flask.abort(flask.Response(
                response="Invalid request: {}".format(x),
                status=400
            ))

    @app.route('/api/game/games', methods=['POST'])
    def create_game():
        return flask.jsonify({'game_id': str(uuid.uuid4())})

    @app.route('/api/game/rolls', methods=['GET'])
    def all_rolls():
        rolls = [r.name for r in game_service.all_rolls()]
        return flask.jsonify(rolls)

    @app.route('/api/game/<game_id>/status', methods=['GET'])
    def game_status(game_id: str):
        is_over = game_service.is_game_over(game_id)
        history = game_service.get_game_history(game_id)

        if not history:
            flask.abort(404)

        roll_lookup = {r.id: r for r in game_service.all_rolls()}
        player_lookup = {p.id: p for p in game_service.all_players()}

        player1 = game_service.find_player_by_id(history[0].player_id)
        player2 = game_service.find_player_by_id(history[1].player_id)

        wins_p1 = game_service.count_round_wins(player1.id, game_id)
        wins_p2 = game_service.count_round_wins(player2.id, game_id)

        data = {
            'is_over': is_over,
            'moves': [h.to_json(roll_lookup[h.roll_id], player_lookup[h.player_id]) for h in history],
            'player1': player1.to_json(),
            'player2': player2.to_json(),
            'winner': player1.to_json() if wins_p1 >= wins_p2 else player2.to_json()
        }

        return flask.jsonify(data)

    @app.route('/api/game/top_scores', methods=['GET'])
    def top_scores():
        players = game_service.all_players()
        wins = [
            {'player': p.to_json(), 'score': game_service.get_win_count(p)}
            for p in players
        ]

        wins.sort(key=lambda wn: -wn.get('score'))
        return flask.jsonify(wins[:10])

    @app.route('/api/game/play_round', methods=['POST'])
    def play_round():
        try:
            db_roll, db_user, game_id = validate_round_request()
            computer_player = game_service.find_player('computer')
            computer_roll = random.choice(game_service.all_rolls())

            game = GameRound(game_id, db_user, computer_player, db_roll, computer_roll)
            game.play()

            return flask.jsonify({
                'roll': db_roll.to_json(),
                'computer_roll': computer_roll.to_json(),
                'player': db_user.to_json(),
                'opponent': computer_player.to_json(),
                'round_outcome': str(game.decision_p1_to_p2),
                'is_final_round': game.is_over,
                'round_number': game.round
            })
        except Exception as x:
            # raise x
            flask.abort(flask.Response(response='Invalid request: {}'.format(x), status=400))

    def validate_round_request():
        if not flask.request.json:
            raise Exception("Invalid request: no JSON body.")
        game_id = flask.request.json.get('game_id')
        if not game_id:
            raise Exception("Invalid request: No game_id value")
        user = flask.request.json.get('user')
        if not user:
            raise Exception("Invalid request: No user value")
        db_user = game_service.find_player(user)
        if not db_user:
            raise Exception("Invalid request: No user with name {}".format(user))
        roll = flask.request.json.get('roll')
        if not roll:
            raise Exception("Invalid request: No roll value")
        db_roll = game_service.find_roll(roll)
        if not db_roll:
            raise Exception("Invalid request: No roll with name {}".format(roll))

        is_over = game_service.is_game_over(game_id)
        if is_over:
            raise Exception("This game is already over.")

        return db_roll, db_user, game_id
