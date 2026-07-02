#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for i in sys.argv[1:]:
        parts = i.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{i}'")
            continue
        if parts[0] in inventory:
            print(f"Redundant item '{parts[0]}' - discarding")
            continue
        try:
            val = int(parts[1])
        except ValueError:
            print(f"Quantity error for '{parts[0]}':")
            print(f"invalid literal for int() with base 10: '{parts[1]}'")
            continue
        inventory[parts[0]] = val

    total_quantity = sum(inventory.values())
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of {len(sys.argv)- 1} items: {total_quantity}")

    for name in inventory.keys():
        print(f"Item {name} represents", end=" ")
        print(f"{(inventory[name] / total_quantity) * 100}%")

    def quantity(k: str) -> int:
        return inventory[k]

    max = 0
    most_abundant = ""
    min = 0
    least_abundant = ""
    for k in inventory.keys():
        if inventory[k] > max:
            max = inventory[k]
            most_abundant = k
        if inventory[k] < min or min == 0:
            min = inventory[k]
            least_abundant = k
    print(f"Item most abundant: {most_abundant}", end=" ")
    print(f"with quantity {inventory[most_abundant]}")
    print(f"Item least abundant: {least_abundant}", end=" ")
    print(f"with quantity {inventory[least_abundant]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
