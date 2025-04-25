import pytest
from app.models.calculator_input import DriverInput
from app.validation.input_validator import validate_driver_input

def test_reject_empty_name():
    driver = DriverInput(name="   ", training_plan="Beginner", horsepower=90, coaching_hours=2, race_entries=1)
    errors = validate_driver_input(driver)
    assert "Driver name is required." in errors

def test_reject_numeric_name():
    driver = DriverInput(name="1234", training_plan="Intermediate", horsepower=200, coaching_hours=1, race_entries=1)
    errors = validate_driver_input(driver)
    assert "Driver name must only contain letters." in errors

def test_reject_negative_hp():
    driver = DriverInput(name="Alex", training_plan="Beginner", horsepower=-50, coaching_hours=1, race_entries=1)
    errors = validate_driver_input(driver)
    assert "Horsepower must be a positive number." in errors

def test_reject_negative_coaching_hours():
    driver = DriverInput(name="Max", training_plan="Elite", horsepower=300, coaching_hours=-2, race_entries=1)
    errors = validate_driver_input(driver)
    assert "Coaching hours must be between 0 and 5." in errors

def test_reject_negative_race_entries():
    driver = DriverInput(name="Lewis", training_plan="Intermediate", horsepower=250, coaching_hours=2, race_entries=-1)
    errors = validate_driver_input(driver)
    assert "Race entries must be 0 or more." in errors

def test_valid_driver_data():
    driver = DriverInput(name="Lando", training_plan="Elite", horsepower=320, coaching_hours=3, race_entries=2)
    errors = validate_driver_input(driver)
    assert errors == []
