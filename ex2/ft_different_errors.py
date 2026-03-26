def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")

    elif operation_number == 1:
        10 / 0

    elif operation_number == 2:
        open("test.txt")

    elif operation_number == 3:
        "hello" + 5

    else:
        print("Operation completed successfully")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    for i in range(5):
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        print()

    try:
        print("Testing multiple errors together...")
        garden_operations(0)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError):
        print("Caught an error (multiple types handled together)!")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_error_types()
