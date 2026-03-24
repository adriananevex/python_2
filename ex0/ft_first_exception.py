def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    try:
        temp = "25"
        print(f"Input data is '{temp}'")
        result = input_temperature(temp)
        print(f"Temperature is now {result}°C\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    try:
        temp = "abc"
        print(f"Input data is '{temp}'")
        result = input_temperature(temp)
        print(f"Temperature is now {result}°C\n")
    except Exception as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
