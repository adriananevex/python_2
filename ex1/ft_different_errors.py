def garden_operations() -> None:
    print("=== Garden Error Types Demo ===\n")

    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print()

    try:
        print("Testing ZeroDivisionError...")
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print()

    try:
        print("Testing FileNotFoundError...")
        file = open("missing.txt")
        file.close()
    except FileNotFoundError as e:
        print(f"Caught FileFoundError: {e}")
    print()

    try:
        print("Testing KeyError...")
        plants = {"tomato": 5}
        print(plants["lettuce"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print()

    try:
        print("Testing multiple errors together...")
        int("abc")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")
    print()

    print("All error types tested successfully!")

if __name__ == "__main__":
    garden_operations()