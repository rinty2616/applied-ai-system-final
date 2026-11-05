
from datetime import date

from pawpal_system import Owner, Pet, Task
from smart_planner import SmartPlanner


def test_smart_planner_valid_schedule():
    owner = Owner("Test Owner", daily_available_minutes=60)
    pet = Pet("Bella", "Dog")
    pet.add_task(Task("Morning walk", "08:00", date.today(), 30, "high"))
    owner.add_pet(pet)

    result = SmartPlanner(owner).create_plan()

    assert result["verified"] is True
    assert result["total_minutes"] == 30
    assert len(result["schedule"]) == 1


def test_smart_planner_conflict():
    owner = Owner("Test Owner", daily_available_minutes=60)
    pet = Pet("Bella", "Dog")
    pet.add_task(Task("Walk", "08:00", date.today(), 30, "high"))
    pet.add_task(Task("Breakfast", "08:15", date.today(), 15, "medium"))
    owner.add_pet(pet)

    result = SmartPlanner(owner).create_plan()

    assert result["verified"] is True
    assert len(result["schedule"]) == 1
    assert len(result["skipped"]) == 1
    assert "overlaps" in result["skipped"][0]


def test_smart_planner_budget():
    owner = Owner("Test Owner", daily_available_minutes=20)
    pet = Pet("Bella", "Dog")
    pet.add_task(Task("Walk", "08:00", date.today(), 30, "high"))
    owner.add_pet(pet)

    result = SmartPlanner(owner).create_plan()

    assert result["verified"] is True
    assert result["total_minutes"] == 0
    assert len(result["skipped"]) == 1
    assert "budget" in result["skipped"][0]
