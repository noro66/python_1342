def water_plants(plant_list):
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise Exception("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")
    print("Testing with error...")
    water_plants(["tomato", None])
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
