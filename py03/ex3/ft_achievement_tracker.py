if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    player_alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    player_bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    player_charlie = {
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist'
        }
    print(f"Player alice achievements: {player_alice}")
    print(f"Player bob achievements: {player_bob}")
    print(f"Player charlie achievements: {player_charlie}")
    print()
    print("=== Achievement Analytics ===")
    uniq_achievement = player_alice.union(player_bob, player_charlie)
    print(f"All unique achievements: {uniq_achievement}")
    print(f"Total unique achievements: {len(uniq_achievement)}")
    print()
    common_achievement = player_alice.intersection(player_bob, player_charlie)
    print(f"Common to all players: {common_achievement}")
    rare_achievement = player_alice.difference(player_bob, player_charlie)
    rare_achievement = rare_achievement.union(
        player_bob.difference(player_alice, player_charlie)
        )
    rare_achievement = rare_achievement.union(
        player_charlie.difference(player_alice, player_bob)
        )
    print(f"Rare achievements (1 player): {rare_achievement}")
    print()
    print(f"Alice vs Bob common: {player_alice.intersection(player_bob)}")
    print(f"Alice unique: {player_alice.difference(player_bob)}")
    print(f"Bob unique: {player_bob.difference(player_alice)}")
