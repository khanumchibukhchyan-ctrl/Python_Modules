#!/usr/bin/env python3

import random
import typing


def main() -> None:
    players = ["alice", "bob", "charlie", "dylan",
               "emma", "gregory", "john", "kevin", "liam"]
    actions = ["move", "grab", "use", "swim", "eat",
               "run", "climb", "release", "sleep"]
    print("=== Game Data Stream Processor ===")

    def gen_event() -> typing.Generator[tuple[str, str], None, None]:
        while True:
            yield (random.choice(players), random.choice(actions))

    def consume_event(events: list[tuple[str, str]]
                      ) -> typing.Generator[tuple[str, str], None, None]:
        while (len(events) > 0):
            event = random.choice(events)
            events.remove(event)
            yield event

    print("=== Game Data Stream Processor ===")

    for i in range(1000):
        event = next(gen_event())
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    list_of_events = []

    for j in range(10):
        list_of_events.append(event)
    print(f"Built list of 10 events: {list_of_events}")

    for event in consume_event(list_of_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {list_of_events}")


if __name__ == "__main__":
    main()
