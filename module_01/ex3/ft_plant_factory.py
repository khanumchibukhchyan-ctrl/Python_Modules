#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age_in_days: int) -> None:
        self.name = name
        self.height = float(height)
        self.age_in_days = age_in_days
        self.growth = 0.65

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_in_days} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.growth, 2)

    def age(self) -> None:
        self.age_in_days += 1


if __name__ == "__main__":
    rose = Plant("Rose",      25,  30)
    oak = Plant("Oak",       200, 365)
    cactus = Plant("Cactus",    5,   90)
    sunflower = Plant("Sunflower", 80,  45)
    fern = Plant("Fern", 15, 120)
    plants = [rose, oak, cactus, sunflower, fern]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()
