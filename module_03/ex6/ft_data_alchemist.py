#!/usr/bin/env python3

import random


def main() -> None:
    print(" === Game Data Alchemist ===")
    print()
    players = ['Alice', 'Bob', 'Charlie', 'Dylan',
               'Emma', 'Gregory', 'John', 'Kevin', 'Liam']

    print(f"Initial list of players: {players}")
    capitalized_players = [name.capitalize() for name in players]
    scores = {name: random.randint(0, 1000) for name in players}
    print("New list with all names capitalized:")
    print(f"{capitalized_players}")
    print("New list of capitalized names only:")
    print(f"{[name for name in players if name[0].isupper()]}")
    print(f"Score dict: {scores}")
    print(f"Score average is {round(sum(scores.values()) / len(scores), 2)}")
    high = [name for name, score in scores.items() if score > 700]
    print(f"High scores: {high}")


if __name__ == "__main__":
    main()
