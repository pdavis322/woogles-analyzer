from typing import TypedDict

class Player(TypedDict):
    user_id: str
    nickname: str
    full_name: str
    country_code: str
    rating: str
    title: str
    is_bot: bool
    first: bool

class GameInfo(TypedDict):
    players: list[Player]
    # TODO: add enum for this
    time_control_name: str
    tournament_id: str
    # TODO: add enum
    game_end_reason: str
    scores: list[int]
    winner: int
    created_at: str
    game_id: str
    last_update: str

