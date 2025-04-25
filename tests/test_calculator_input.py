import pytest
from app.models.calculator_input import DriverInput

def test_valid_category_resolution():
    driver = DriverInput("Lewis", "Beginner", horsepower=85, coaching_hours=2, race_entries=0)
    assert driver.category == "Entry-Level"

def test_race_eligibility_check():
    elite = DriverInput("Seb", "Elite", 250, 3, 2)
    beginner = DriverInput("Max", "Beginner", 95, 1, 0)

    assert elite.is_race_eligible() is True
    assert beginner.is_race_eligible() is False

def test_post_init_variable_type():
    driver = DriverInput("Charles", "Intermediate", "180", "2", "1")
    assert isinstance(driver.horsepower, int)
    assert isinstance(driver.coaching_hours, int)
    assert isinstance(driver.race_entries, int)

def test_invalid_horsepower_raises():
    with pytest.raises(ValueError, match="Horsepower must be a valid number."):
        DriverInput("Invalid", "Beginner", "abc", 1, 1)

def test_invalid_coaching_hours_raises():
    with pytest.raises(ValueError, match="Coaching hours must be a valid number."):
        DriverInput("Invalid", "Beginner", 100, "oops", 0)

def test_invalid_race_entries_raises():
    with pytest.raises(ValueError, match="Race entries must be a valid number."):
        DriverInput("Invalid", "Beginner", 100, 1, "NaN")

def test_driver_str_output():
    driver = DriverInput("Lando", "Intermediate", 190, 2, 1)
    output = str(driver)
    assert "Plan: Intermediate" in output
    assert "HP: 190" in output
    assert "Coaching: 2" in output
    assert "Races: 1" in output
