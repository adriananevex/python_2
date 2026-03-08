def check_temperature(temp_str: str) -> int:
    try:
        temperature = int(temp_str)

        if temperature < 0:
            raise ValueError(
                f"{temperature}°C is too cold for plants (min 0°C)"
            )
        if temperature > 40:
            raise ValueError(
                f"{temperature}°C is too hot for plants (max 40°C)"
            )

        return temperature

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")

    test_values = ["25", "abc", "100", "-50"]

    for value in test_values:
        print(f"Testing temperature: {value}")

        result = check_temperature(value)

        if result is not None:
            print(f"Temperature {result}°C is perfect for plants!")

        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
