#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)

def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    print("Input data is '25'")
    temp = input_temperature("25")
    print(f"Temperature is now {temp}°C\n")

    print("Input data is 'abc'")

    try:
        temp = input_temperature("abc")
        print(f"Temperature is now {temp}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests complited - program didn't crash!")


if __name__ == "__main__":
    test_temperature()