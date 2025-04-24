from dataclasses import dataclass
from app.calculations.category_resolver import get_category_from_hp

@dataclass
class DriverInput:
    name: str
    training_plan: str
    horsepower: int
    coaching_hours: int
    race_entries: int

    def __post_init__(self): # Attach attributes in correct variable type
        try:
            self.horsepower = int(self.horsepower)
        except ValueError:
            raise ValueError("Horsepower must be a valid number.")

        try:
            self.coaching_hours = int(self.coaching_hours)
        except ValueError:
            raise ValueError("Coaching hours must be a valid number.")

        try:
            self.race_entries = int(self.race_entries)
        except ValueError:
            raise ValueError("Race entries must be a valid number.")
        
    @property
    def category(self) -> str: # Identify racing category based on horsepower
        return get_category_from_hp(self.horsepower)

    def is_race_eligible(self) -> bool: # Determine if the driver can enter races
        return self.training_plan in ("Intermediate", "Elite")

    def __str__(self): # For logging visability
        return (
            f"Plan: {self.training_plan}, "
            f"HP: {self.horsepower}, "
            f"Coaching: {self.coaching_hours}, "
            f"Races: {self.race_entries}"
        )
