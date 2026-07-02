#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    valid_scores = []

    for arg in sys.argv[1:]:
        try:
            score = int(arg)
            valid_scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if (len(valid_scores) == 0):
        print("No scores provided. Usage:"
              " python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print("Scores processed:", valid_scores)
        print("Total players:", len(valid_scores))
        print("Total score:", sum(valid_scores))
        print("Average score:", sum(valid_scores) / len(valid_scores))
        print("High score:", max(valid_scores))
        print("Low score:", min(valid_scores))
        print("Score range:", max(valid_scores) - min(valid_scores))


if __name__ == "__main__":
    main()
