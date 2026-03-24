def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")

    elif operation_number == 1:
        10 / 0

    elif operation_number == 2:
        open("file_that_does_not_exist.txt")

    elif operation_number == 3:
        "hello" + 5 # type: ignore

    else:
        print("No error for this operation.")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    for i in range(4):
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
        except ValueError:
            print("Caught ValueError: invalid data provided!")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: cannot divide by zero!")
        except FileNotFoundError:
            print("Caught FileNotFoundError: file does not exist!")
        except TypeError:
            print("Caught TypeError: incompatible types!")
        print()

    try:
        print("Testing multiple errors together...")
        garden_operations(0)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError):
        print("Caught an error (multiple types handled together)!")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_error_types()
