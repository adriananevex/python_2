def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int,
) -> str:
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1 or water_level > 10:
        raise ValueError(
            f"Water level {water_level} is invalid (1-10 allowed)"
        )

    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is invalid (2-12 allowed)"
        )

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("== Garden Plant Health Checker ===\n")

    try:
        print("Testing good values...")
        print(check_plant_health("tomato", 5, 8))
    except ValueError as e:
        print(f"Error: {e}")

    try:
        print("\nTetsing empty plant name...")
        print(check_plant_health("tomato", 5, 8))
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
