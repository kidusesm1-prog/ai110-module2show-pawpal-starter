from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    description: str
    time: str
    frequency: str = "once"
    completed: bool = False

    def mark_complete(self):
        """Mark this task as completed."""
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet."""
        pass

    def get_tasks(self):
        """Return this pet's tasks."""
        pass


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to this owner."""
        pass

    def get_all_tasks(self):
        """Return all tasks for all pets."""
        pass


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_today_schedule(self):
        """Return today's tasks."""
        pass

    def sort_by_time(self, tasks):
        """Sort tasks by time."""
        pass

    def filter_by_pet(self, pet_name):
        """Filter tasks by pet name."""
        pass

    def detect_conflicts(self):
        """Detect tasks scheduled at the same time."""
        pass