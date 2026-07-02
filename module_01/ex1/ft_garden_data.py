#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age_in_days: int) -> None:
        self.name = name
        self.height = height
        self.age_in_days = age_in_days

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_in_days} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)

    sunflower = Plant("Sunflower", 80, 45)

    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()
