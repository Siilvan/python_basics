import random


def ft_data_alchemist() -> None:
    print('=== Game Data Alchemist ===')
    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
               'Gregory', 'john', 'kevin', 'Liam']
    p_capitalized = [p.capitalize() for p in players]
    p_init_capital = [p for p in players if p == p.capitalize()]
    score_dict = {p: random.randrange(50, 1000) for p in p_capitalized}
    average = sum(score_dict[p] for p in score_dict.keys())/len(score_dict)
    high_scores_dict = {p: score for p, score
                        in score_dict.items() if score > average}

    print(f'Initial list of players: {players}')
    print(f'New list with all names capitalized: {p_capitalized}')
    print(f'New list of capitalized names only: {p_init_capital}')
    print(f'Score dict: {score_dict}')
    print(f'Score average is: {average:.2f}')
    print(f'High scores: {high_scores_dict}')


if __name__ == "__main__":
    ft_data_alchemist()
