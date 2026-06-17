#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
         super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
         super().__init__(message)

def check_plant() -> None:
    raise PlantError("The tomato plant is wilting!")

def water_plant(plant_name) -> None:

	plants = ["Tomato", "Lettuce", "Carrots"]

	if plant_name not in plants:
		raise PlantError(f"Invalid plant name to water: '{plant_name}'")

	print(f"Watering {plant_name}: [OK]")

def test_watering_system() -> None:
    
    print("Opening watering system")

    try:

        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")
    except PlantError as e:

        print(f"Caught PlantError: {e}")

        print(".. ending tests and returning to main")

        return
    
    finally:

        print("Closing watering system")

def main():

    print("=== Garden Watering System ===")

    print("Testing plants...")

    test_watering_system()

    print("Cleanup always happens, even with errors!")

if __name__ == "__main__":
	main()