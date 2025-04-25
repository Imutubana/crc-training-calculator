import pytest
from app.models.calculator_input import DriverInput
from app.calculations.cost_calculator import (
    calculate_training_cost,
    calculate_private_coaching_cost,
    calculate_race_cost,
    itemised_cost_list
)

def test_calculate_training_cost():
    assert calculate_training_cost("Beginner") == 120.0 
    assert calculate_training_cost("Intermediate") == 160.0 
    assert calculate_training_cost("Elite") == 200.0

def test_calculate_private_coaching_cost():
    assert calculate_private_coaching_cost(0) == 0.0
    assert calculate_private_coaching_cost(3) == 45.0
    assert calculate_private_coaching_cost(5) == 75.0

def test_calculate_race_cost():
    assert calculate_race_cost(0) == 0.0
    assert calculate_race_cost(2) == 70.0
    assert calculate_race_cost(4) == 140.0

def test_get_itemised_cost_totals():
    driver = DriverInput(
        name="Test",
        training_plan="Intermediate",
        horsepower=150,
        coaching_hours=2,
        race_entries=1
    )
    costs = itemised_cost_list(driver)

    assert costs.training_cost == 160.0
    assert costs.coaching_cost == 30.0
    assert costs.racing_cost == 35.0
    assert costs.total_cost == 225.0
