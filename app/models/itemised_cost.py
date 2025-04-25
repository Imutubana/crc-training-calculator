from dataclasses import dataclass

@dataclass
class ItemisedCost:
    training_cost: float
    coaching_cost: float
    racing_cost: float

    def __str__(self) -> str:
        return (
            f"Training costs: £{self.training_cost:.2f}\n"
            f"Coaching costs: £{self.coaching_cost:.2f}\n"
            f"Racing costs: £{self.racing_cost:.2f}\n"
            f"Total: £{self.total_cost:.2f}"
        )
    
    @property
    def total_cost(self) -> float:
        return self.training_cost + self.coaching_cost + self.racing_cost
