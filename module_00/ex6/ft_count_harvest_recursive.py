def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def count_days(day: int) -> None:
        if day > days:
            print("Harvest time!")
            return
        else:
            print(f"Day {day}")
            count_days(day + 1)
    count_days(1)
