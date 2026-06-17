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

    try:
        temp = input_temperature("100")
        if temp > 40:
            print(f"Temperature is now {temp}°C")
            raise Exception("100°C is too hot for plants (max 40°C)")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    try:
        temp = input_temperature("-50")
        if temp < 0:
            print(f"Temperature is now {temp}°C")
            raise Exception("-50°C is too cold for plants (min 0°C)")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests complited - program didn't crash!")


if __name__ == "__main__":
    test_temperature()