#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age_in_days: int) -> None:
        self._name = name
        self._height = height
        self._age_in_days = age_in_days
        self._growth = 0.65

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age_in_days} days old")

    def grow(self) -> None:
        self._height = round(self._height + self._growth, 2)

    def age(self) -> None:
        self._age_in_days += 1


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_in_days: int,
        color: str
    ) -> None:
        super().__init__(name, height, age_in_days)
        self._color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def bloom(self) -> None:
        print(f"[asked the {self._name} to bloom]")
        self._bloomed = True


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_in_days: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age_in_days)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"[asked the {self._name} to produce shade]")
        print(f"{self._name} now produces a shade of", end=" ")
        print(f"{self._height}cm long and {self._trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age_in_days: int,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, age_in_days)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 1

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    # === Flower ===
    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    # === Tree ===
    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    # === Vegetable ===
    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    days = 20
    for _ in range(days):
        tomato.grow()
        tomato.age()
    tomato.show()
