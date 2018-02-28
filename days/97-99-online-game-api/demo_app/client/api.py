import uplink

from uplink_helpers import raise_for_status, response_to_data


@response_to_data
@raise_for_status
@uplink.json
class GameService(uplink.Consumer):
    def __init__(self):
        super().__init__(base_url='http://localhost:5000')

    @uplink.get('/api/game/users/{username}')
    def find_user(self, username):
        pass

    @uplink.put('/api/game/users')
    def create_user(self, **kwargs: uplink.Body):
        pass

    @uplink.post('/api/game/games')
    def create_game(self, **kwargs: uplink.Body):
        pass

    @uplink.get('/api/game/rolls')
    def all_rolls(self):
        pass

    @uplink.get('/api/game/{game_id}/status')
    def game_status(self, game_id):
        pass

    @uplink.get('/api/game/top_scores')
    def top_scores(self):
        pass

    @uplink.post('/api/game/play_round')
    def play_round(self, **kwargs: uplink.Body):
        pass
