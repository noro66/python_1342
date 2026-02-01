from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform

try:
    print("=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()

    print("Registering Tournament Cards...")

    fire_dragon = TournamentCard("Fire Dragon", 6, "Legendary", 8, 7)
    ice_wizard = TournamentCard("Ice Wizard", 4, "Epic", 6, 5)
    ice_wizard.base_rating = 1150

    dragon_id = "dragon_001"
    wizard_id = "wizard_001"
    platform.registered_cards[dragon_id] = fire_dragon
    platform.registered_cards[wizard_id] = ice_wizard

    print(f"{fire_dragon.name} (ID: {dragon_id}):")
    stats = fire_dragon.get_tournament_stats()
    print(f"- Interfaces: {stats['interfaces']}")
    print(f"- Rating: {stats['rating']}")
    print(f"- Record: {stats['record']}")

    print(f"{ice_wizard.name} (ID: {wizard_id}):")
    stats = ice_wizard.get_tournament_stats()
    print(f"- Interfaces: {stats['interfaces']}")
    print(f"- Rating: {stats['rating']}")
    print(f"- Record: {stats['record']}")

    print("\nCreating tournament match...")

    fire_dragon.update_wins(1)
    ice_wizard.update_losses(1)
    platform.matches_played = 1

    match_result = {
        'winner': dragon_id,
        'loser': wizard_id,
        'winner_rating': fire_dragon.calculate_rating(),
        'loser_rating': ice_wizard.calculate_rating()
    }
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, entry in enumerate(leaderboard, 1):
        print(
            f"{i}. {entry['name']} - Rating:",
            f"{entry['rating']} ({entry['record']})"
            )

    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")

except Exception as e:
    print("ERROR:", e)
