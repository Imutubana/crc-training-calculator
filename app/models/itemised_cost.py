from dataclasses import dataclass
from app.constants import training_plans

@dataclass
class ItemisedCost:
    training_cost: float
    coaching_cost: float
    racing_cost: float
    plan_name: str

    def __str__(self) -> str:
        training_plan_price = training_plans.TRAINING_PLANS[self.plan_name]["weekly_price"]
        training_plan_sessions = training_plans.TRAINING_PLANS[self.plan_name]["sessions_per_week"]
        return (
            f"Training costs: £{self.training_cost:.2f} @ £{training_plan_price:.2f} per hour ({training_plan_sessions:.0f} sessions per week)\n"
            f"Coaching costs: £{self.coaching_cost:.2f} @ £{training_plans.PRIVATE_TUITION_PRICE:.2f} per hour\n"
            f"Racing costs: £{self.racing_cost:.2f} @ £{training_plans.RACE_ENTRY_FEE:.2f} per entry\n"
            f"Total: £{self.total_cost:.2f}"
        )
    
    @property
    def total_cost(self) -> float:
        return self.training_cost + self.coaching_cost + self.racing_cost
