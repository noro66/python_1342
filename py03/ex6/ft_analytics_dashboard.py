sample_game_data = {
    'players': {
        'alice': {
            'level': 41,
            'total_score': 2824,
            'sessions_played': 13,
            'favorite_mode': 'ranked',
            'achievements_count': 5
        },
        'bob': {
            'level': 16,
            'total_score': 4657,
            'sessions_played': 47,
            'favorite_mode': 'ranked',
            'achievements_count': 2
        },
        'charlie': {
            'level': 44,
            'total_score': 9935,
            'sessions_played': 21,
            'favorite_mode': 'ranked',
            'achievements_count': 7
        },
        'diana': {
            'level': 3,
            'total_score': 1488,
            'sessions_played': 21,
            'favorite_mode': 'casual',
            'achievements_count': 4
        },
        'eve': {
            'level': 33,
            'total_score': 1434,
            'sessions_played': 81,
            'favorite_mode': 'casual',
            'achievements_count': 7
        },
        'frank': {
            'level': 15,
            'total_score': 8359,
            'sessions_played': 85,
            'favorite_mode': 'competitive',
            'achievements_count': 1
        }
    },
    'sessions': [
        {'player': 'bob', 'duration_minutes': 94, 'score': 1831,
         'mode': 'competitive', 'completed': False},
        {'player': 'bob', 'duration_minutes': 32, 'score': 1478,
         'mode': 'casual', 'completed': True},
        {'player': 'diana', 'duration_minutes': 17, 'score': 1570,
         'mode': 'competitive', 'completed': False},
        {'player': 'alice', 'duration_minutes': 98, 'score': 1981,
         'mode': 'ranked', 'completed': True},
        {'player': 'diana', 'duration_minutes': 15, 'score': 2361,
         'mode': 'competitive', 'completed': False},
        {'player': 'eve', 'duration_minutes': 29, 'score': 2985,
         'mode': 'casual', 'completed': True},
        {'player': 'frank', 'duration_minutes': 34, 'score': 1285,
         'mode': 'casual', 'completed': True},
        {'player': 'alice', 'duration_minutes': 53, 'score': 1238,
         'mode': 'competitive', 'completed': False},
        {'player': 'bob', 'duration_minutes': 52, 'score': 1555,
         'mode': 'casual', 'completed': False},
        {'player': 'frank', 'duration_minutes': 92, 'score': 2754,
         'mode': 'casual', 'completed': True},
        {'player': 'eve', 'duration_minutes': 98, 'score': 1102,
         'mode': 'casual', 'completed': False},
        {'player': 'diana', 'duration_minutes': 39, 'score': 2721,
         'mode': 'ranked', 'completed': True},
        {'player': 'frank', 'duration_minutes': 46, 'score': 329,
         'mode': 'casual', 'completed': True},
        {'player': 'charlie', 'duration_minutes': 56, 'score': 1196,
         'mode': 'casual', 'completed': True},
        {'player': 'eve', 'duration_minutes': 117, 'score': 1388,
         'mode': 'casual', 'completed': False},
        {'player': 'diana', 'duration_minutes': 118, 'score': 2733,
         'mode': 'competitive', 'completed': True},
        {'player': 'charlie', 'duration_minutes': 22, 'score': 1110,
         'mode': 'ranked', 'completed': False},
        {'player': 'frank', 'duration_minutes': 79, 'score': 1854,
         'mode': 'ranked', 'completed': False},
        {'player': 'charlie', 'duration_minutes': 33, 'score': 666,
         'mode': 'ranked', 'completed': False},
        {'player': 'alice', 'duration_minutes': 101, 'score': 292,
         'mode': 'casual', 'completed': True},
        {'player': 'frank', 'duration_minutes': 25, 'score': 2887,
         'mode': 'competitive', 'completed': True},
        {'player': 'diana', 'duration_minutes': 53, 'score': 2540,
         'mode': 'competitive', 'completed': False},
        {'player': 'eve', 'duration_minutes': 115, 'score': 147,
         'mode': 'ranked', 'completed': True},
        {'player': 'frank', 'duration_minutes': 118, 'score': 2299,
         'mode': 'competitive', 'completed': False},
        {'player': 'alice', 'duration_minutes': 42, 'score': 1880,
         'mode': 'casual', 'completed': False},
        {'player': 'alice', 'duration_minutes': 97, 'score': 1178,
         'mode': 'ranked', 'completed': True},
        {'player': 'eve', 'duration_minutes': 18, 'score': 2661,
         'mode': 'competitive', 'completed': True},
        {'player': 'bob', 'duration_minutes': 52, 'score': 761,
         'mode': 'ranked', 'completed': True},
        {'player': 'eve', 'duration_minutes': 46, 'score': 2101,
         'mode': 'casual', 'completed': True},
        {'player': 'charlie', 'duration_minutes': 117, 'score': 1359,
         'mode': 'casual', 'completed': True}
    ],
    'game_modes': ['casual', 'competitive', 'ranked'],
    'achievements': ['first_blood', 'level_master', 'speed_runner',
                     'treasure_seeker', 'boss_hunter', 'pixel_perfect',
                     'combo_king', 'explorer']
}


def list_comprehensions(sample_data):
    print("=== List Comprehension Examples ===")
    hight_score_list = [
                        player
                        for player, details in sample_data["players"].items()
                        if details["total_score"] > 2000
                        ]
    score_doubled = [
     details["total_score"] * 2
     for _, details in sample_data["players"].items()
    ]
    active_players = [
        player
        for player, details in sample_data["players"].items()
        if details["sessions_played"] > 45
    ]
    print(f"High scorers (>2000): {hight_score_list}")
    print(f"Scores doubled: {score_doubled}")
    print(f"Active players: {active_players}")
    print()


def dict_comprehensions(sample_data):
    print("=== Dict Comprehension Examples ===")
    player_scores = {
        player: details["total_score"]
        for player, details in sample_data["players"].items()
    }
    mode_types_played = {
        session["mode"]:  sum([1 if ses["mode"] == session["mode"] else 0
                               for ses in sample_data["sessions"]])
        for session in sample_data['sessions']
    }
    achievement_counts = {
        name: details["achievements_count"]
        for name, details in sample_data["players"]
    }
    print(f"Player scores: {player_scores}")
    print(f"mode type played : {mode_types_played}")
    print(f"Achievement counts: {achievement_counts}")


def set_comprehensions(sample_data):
    pass


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")
    print()
    list_comprehensions(sample_game_data)
    dict_comprehensions(sample_game_data)
