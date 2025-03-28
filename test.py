import requests
from typing import cast
from .woogles_types import Player, GameInfo

username = 'jcv71'
num_games = 2

BASE_URL = 'https://woogles.io/api'
API_KEY = '6Mcooc5xJ9Z9UXCHGYubohmhAb9tkm89PqnY9Eu5JjBB'

recent_games = requests.post(BASE_URL + '/game_service.GameMetadataService/GetRecentGames', 
                             headers={'Content-Type': 'application/json', 'X-Api-Key': API_KEY}, 
                             json={
                                 'username': username,
                                 'num_games': num_games,
                                 'offset': 0
                             })

game_ids = [game['game_id'] for game in recent_games.json()['game_info']]
    
print(game_ids)



