import sys


def ft_score_analytics() -> None:
    args = sys.argv
    scores: list[int] = []
    print("=== Player Score Analytics ===")
    for arg in args[1:]:
        try:
            score = int(arg)
            scores += [score]
        except ValueError:
            print(f"Invalid parameter: {arg}")
    if len(scores) == 0:
        print("No scored provided. Usage: python3"
              "ft_score_analytics.py <score1> <score2> ...")
        return
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total socre: {sum(scores)}")
    print(f"Average score: {sum(scores)/len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    ft_score_analytics()
