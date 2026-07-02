#!/usr/bin/env python3

class Plant:
    class Counter:
        def __init__(self) -> None:
            self._growth = 0
            self._age_in_days = 0
            self._show = 0

        def display(self) -> None:
            print(f"Stats: {self._growth} grow", end=", ")
            print(f"{self._age_in_days} age, {self._show} show")

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

    @staticmethod
    def is_older_than_year(age_in_days: int) -> bool:
        return age_in_days > 356

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


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
        self._bloomed = True


class Tree(Plant):
    class TreeCounter(Plant.Counter):
        def __init__(self) -> None:
            super().__init__()
            self._shade = 0

        def display(self) -> None:
            super().display()
            print(f"{self._shade} shade")

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


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age_in_days: int,
        color: str
    ) -> None:
        super().__init__(name, height, age_in_days, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds += 1

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


if __name__ == "__main__":
    print("=== Garden statistics ===")

    # --- Check year-old ---
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    # --- Flower ---
    print("=== Flower")
    rose_counter = Plant.Counter()
    rose = Flower("Rose", 15.0, 10, "red")

    rose.show()
    rose_counter._show += 1
    print("[statistics for Rose]")
    rose_counter.display()

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose_counter._growth += 1
    rose.bloom()
    rose.show()
    rose_counter._show += 1
    print("[statistics for Rose]")
    rose_counter.display()

    # --- Tree ---
    print("=== Tree")
    oak_counter = Tree.TreeCounter()
    oak = Tree("Oak", 200.0, 365, 5.0)

    oak.show()
    oak_counter._show += 1
    print("[statistics for Oak]")
    oak_counter.display()

    print("[asking the oak to produce shade]")
    print("Tree ", end="")
    oak.produce_shade()
    oak_counter._shade += 1
    print("[statistics for Oak]")
    oak_counter.display()

    # --- Seed ---
    print("=== Seed")
    sunflower_counter = Plant.Counter()
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")

    sunflower.show()
    sunflower_counter._show += 1

    print("[make sunflower grow, age and bloom]")
    for _ in range(46):
        sunflower.grow()
    sunflower_counter._growth += 1
    for _ in range(20):
        sunflower.age()
    sunflower_counter._age_in_days += 1
    sunflower.bloom()
    sunflower.show()
    sunflower_counter._show += 1
    print("[statistics for Sunflower]")
    sunflower_counter.display()

    # --- Anonymous ---
    print("=== Anonymous")
    anon_counter = Plant.Counter()
    anon = Plant.anonymous()
    anon.show()
    anon_counter._show += 1
    print("[statistics for Unknown plant]")
    anon_counter.display()