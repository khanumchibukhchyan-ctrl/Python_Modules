#!/usr/bin/env python3

def garden_operation(operation_number: str) -> str:
    if int(operation_number) == 0:
        x = int("abc")

    elif int(operation_number) == 1:
        x = 10 / 0

    elif int(operation_number) == 2:
        x = open("non_existing.txt", "r")

    elif int(operation_number) == 3:
        x = "10" + 5 # type: ignore
    
    else:
        return "No error"

def test_error_types() -> None:
    print("=== Garden Error Tests ===")

    for i in range(5):
        print(f"\nTesting operation {i}...")

        try:
            garden_operation(i)
            print("Operation completed successfully")
    
        except ValueError as e:
            print(f"Caught ValueError: {e}")
    
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
    
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
    
        except TypeError as e:
            print(f"Caught TypeError: {e}")

    print("\nAll tests completed - program didn't crash!")

if __name__ == "__main__":
    test_error_types()