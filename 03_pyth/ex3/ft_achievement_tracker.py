import random

ACHIEVEMENTS = ['Crafting Genius', 'Strategist', 'World Savior',
                'Speed Runner', 'Survivor', 'Master Explorer',
                'Treasure Hunter', 'Unstoppable', 'First Steps',
                'Collector Supreme', 'Untouchable', 'Sharp Mind',
                'Boss Slayer']


def gen_player_achievements() -> set[str]:
    return set(random.sample(ACHIEVEMENTS, random.randint(5, 10)))


def ft_achievement_tracker() -> None:
    players = ['Alice', 'Bob', 'Charlie', 'Dylan']
    p_achievements = {player: gen_player_achievements() for player in players}
    all_achievements = [p_achievements[player] for player in players]

    for player in players:
        print(f"Player {player}: {p_achievements[player]}")
    print(f"\nAll distinct achievements: {ACHIEVEMENTS}")
    print(f"\nCommon achievements: {set.intersection(*all_achievements)}\n")

    for player in players:
        others = [p_achievements[other]
                  for other in players if other is not player]
        print(f"Only {player} has: "
              f"{p_achievements[player].difference(*others)}")

    print("")
    for player in players:
        print(f"{player} is missing: "
              f"{set(ACHIEVEMENTS).difference(p_achievements[player])}")


if __name__ == "__main__":
    ft_achievement_tracker()
