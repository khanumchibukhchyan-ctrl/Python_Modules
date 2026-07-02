#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age_in_days: int) -> None:
        self._name = name
        self._height = 0.0
        self._age_in_days = 0
        self._growth = 0.65

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = float(height)

        if age_in_days < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age_in_days = age_in_days

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age_in_days} days old")

    def grow(self) -> None:
        self._height = round(self._height + self._growth, 2)

    def age(self) -> None:
        self._age_in_days += 1

    def get_age(self) -> int:
        return self._age_in_days

    def get_height(self) -> float:
        return self._height

    def set_age(self, age_in_days: int) -> None:
        if age_in_days < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_in_days = age_in_days
            print(f"Age update: {age_in_days} days")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height update: {height} cm")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15, 10)
    print("Plant created: ", end="")
    rose.show()

    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-5)
    rose.set_age(-10)

    print("Current state: ", end="")
    rose.show()
