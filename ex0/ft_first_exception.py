def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    try:
        temp = "25"
        
        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
