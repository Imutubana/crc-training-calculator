from app.constants.training_plans import TRAINING_PLANS, PRIVATE_TUITION_PRICE, RACE_ENTRY_FEE
from app.models.calculator_input import DriverInput
from app.models.itemised_cost import ItemisedCost

def calculate_training_cost(plan_name: str) -> float:
    weekly_price = TRAINING_PLANS[plan_name]["weekly_price"]
    return weekly_price * 4  # Assume 4 weeks per month

def calculate_private_coaching_cost(hours: int) -> float:
    return hours * PRIVATE_TUITION_PRICE

def calculate_race_cost(entries: int) -> float:
    return entries * RACE_ENTRY_FEE

def itemised_cost_list(input_driver_data:DriverInput) -> ItemisedCost:
    training_costs = calculate_training_cost(input_driver_data.training_plan)
    coaching_costs = calculate_private_coaching_cost(input_driver_data.coaching_hours)
    racing_costs = calculate_race_cost(input_driver_data.race_entries)

    return ItemisedCost(
        training_cost=training_costs,
        coaching_cost=coaching_costs,
        racing_cost=racing_costs
    )

def get_list_category_names():
    training_plans = list(TRAINING_PLANS.keys())
    return training_plans
