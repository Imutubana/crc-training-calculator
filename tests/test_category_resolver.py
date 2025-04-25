import pytest
from app.calculations.category_resolver import get_category_from_hp

@pytest.mark.parametrize("hp,expected_category", [
    (0, "Entry-Level"),
    (50, "Entry-Level"),
    (99, "Entry-Level"),
    (100, "Sport"),
    (150, "Sport"),
    (199, "Sport"),
    (200, "Performance"),
    (250, "Performance"),
    (299, "Performance"),
    (300, "High-Performance"),
    (350, "High-Performance"),
    (399, "High-Performance"),
    (400, "Supercar"),
    (500, "Supercar"),
    (1000, "Supercar"),
])
def test_get_category_from_hp(hp, expected_category):
    assert get_category_from_hp(hp) == expected_category
