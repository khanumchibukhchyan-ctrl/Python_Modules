#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age_in_days: int) -> None:
        self.name = name
        self.height = height
        self.age_in_days = age_in_days
        self.growth = 0.65

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_in_days} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.growth, 2)

    def age(self) -> None:
        self.age_in_days += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)

    print("=== Garden Plant Registry ===")
    rose.show()

    start_h = rose.height

    for day in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {day} ===")
        rose.show()

    growth = round(rose.height - start_h, 2)
    print(f"Growth in 7 days: {growth}cm")
