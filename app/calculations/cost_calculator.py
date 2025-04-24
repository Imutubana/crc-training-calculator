from app.training_plans import TRAINING_PLANS, PRIVATE_TUITION_PRICE, RACE_ENTRY_FEE
from app.models.calculator_input import DriverInput

def calculate_training_cost(plan_name: str) -> float:
    weekly_price = TRAINING_PLANS[plan_name]["weekly_price"]
    return weekly_price * 4  # Assume 4 weeks per month

def calculate_private_coaching_cost(hours: int) -> float:
    return hours * PRIVATE_TUITION_PRICE

def calculate_race_cost(entries: int) -> float:
    return entries * RACE_ENTRY_FEE

def calculate_total_cost(input_driver_data:DriverInput) -> float:
    return (
        calculate_training_cost(input_driver_data.training_plan) +
        calculate_private_coaching_cost(input_driver_data.coaching_hours) +
        calculate_race_cost(input_driver_data.race_entries)
    )

def get_list_category_names():
    training_plans = list(TRAINING_PLANS.keys())
    return training_plans
