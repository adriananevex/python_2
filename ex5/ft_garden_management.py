class GardenError(Exception):
    pass


class InvalidPlantNameError(GardenError):
    pass


class WaterLevelError(GardenError):
    pass


class SunlightLevelError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants: dict[str, dict[str, int]] = {}
        self.max_water = 10
        self.max_sun = 10

    def add_plant(self, name: str, water: int, sun: int) -> None:
        if not name.strip():
            raise InvalidPlantNameError("Plant name cannot be empty")
        if water < 0 or sun < 0:
            raise GardenError("Water and sun levels must be non-negative!")
        self.plants[name] = {"water": water, "sun": sun}
        print(f"Added {name} successfully")

    def water_plant(self, name: str, amount: int) -> None:
        if name not in self.plants:
            raise GardenError(f"Plant {name} does not exist")
        if amount <= 0:
            raise GardenError("Water amount must be positive")

        print(f"Watering {name} - start")
        try:
            self.plants[name]["water"] += amount
            if self.plants[name]["water"] > self.max_water:
                raise WaterLevelError(
                    f"Water level {self.plants[name]['water']} "
                    f"is too high (max {self.max_water})"
                )
            print(f"Watering {name} - success")
        except WaterLevelError as e:
            print(f"Error watering {name}: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, name: str) -> None:
        if name not in self.plants:
            raise GardenError(f"Plant {name} does not exist")

        water = self.plants[name]["water"]
        sun = self.plants[name]["sun"]
        if water > self.max_water:
            raise WaterLevelError(
                f"Water level {water} is too high (max {self.max_water})"
            )
        if sun > self.max_sun:
            raise SunlightLevelError(
                f"Sunlight level {sun} is too high (max {self.max_sun})"
            )

        status = "healthy"
        print(f"{name}: {status} (water: {water}, sun: {sun})")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    garden = GardenManager()

    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato", 5, 8)
        garden.add_plant("lettuce", 3, 4)
        garden.add_plant("", 2, 3)
    except GardenError as e:
        print(f"Error adding plant: {e}")

    print("Watering plants...")
    try:
        garden.water_plant("tomato", 2)
        garden.water_plant("lettuce", 20)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("Checking plant health...")
    for plant_name in ["tomato", "lettuce"]:
        try:
            garden.check_health(plant_name)
        except GardenError as e:
            print(f"Error checking {plant_name}: {e}")

    print("Testing error recovery...")
    try:
        garden.water_plant("carrot", 5)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...")

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
