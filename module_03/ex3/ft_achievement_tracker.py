#!/usr/bin/env python3

import random


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()

    achievements = {"Crafting Genius", "Strategist",
                    "World Savior", "Speed Runner", "Survivor",
                    "Master Explorer", "Treasure Hunter",
                    "Unstoppable", "First Steps", "Collector Supreme",
                    "Untouchable", "Sharp Mind", "Boss Slayer"}

    def gen_player_achievements() -> set[str]:
        count = random.randint(1, len(achievements))
        return set(random.sample(achievements, count))

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print("Player Alice:", alice)
    print("Player Bob:", bob)
    print("Player Charlie:", charlie)
    print("Player Dylan:", dylan)
    print()
    print("All distinct achievements:", achievements)
    print()
    common = set.intersection(
        alice,
        bob,
        charlie,
        dylan
    )
    print("Common achievements:", common)
    print()
    only_alice = set.difference(alice, bob, charlie, dylan)
    only_bob = set.difference(bob, alice, charlie, dylan)
    only_charlie = set.difference(charlie, alice, bob, dylan)
    only_dylan = set.difference(dylan, alice, bob, charlie)
    print("Only Alice has:", only_alice)
    print("Only Bob has:", only_bob)
    print("Only Charlie has:", only_charlie)
    print("Only Dylan has:", only_dylan)
    print()
    print("Alice is missing:", set.difference(achievements, alice))
    print("Bob is missing:", set.difference(achievements, bob))
    print("Charlie is missing:", set.difference(achievements, charlie))
    print("Dylan is missing:", set.difference(achievements, dylan))


if __name__ == "__main__":
    main()
