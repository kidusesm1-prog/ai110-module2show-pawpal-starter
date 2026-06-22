from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class Task:
    description: str
    time: str
    frequency: str = "once"
    completed: bool = False

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self):
        """Return this pet's tasks."""
        return self.tasks


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to this owner."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Tuple[Pet, Task]]:
        """Return all tasks for all pets."""
        all_tasks = []

        for pet in self.pets:
            for task in pet.get_tasks():
                all_tasks.append((pet, task))

        return all_tasks


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def get_today_schedule(self):
        """Return today's tasks."""
        return self.owner.get_all_tasks()

    def sort_by_time(self, tasks):
        """Sort tasks by time."""
        return sorted(tasks, key=lambda item: item[1].time)

    def filter_by_pet(self, pet_name):
        """Filter tasks by pet name."""
        return [
            (pet, task)
            for pet, task in self.owner.get_all_tasks()
            if pet.name.lower() == pet_name.lower()
        ]

    def detect_conflicts(self):
        """Detect tasks scheduled at the same time."""
        conflicts = []
        seen_times = {}

        for pet, task in self.owner.get_all_tasks():
            if task.time in seen_times:
                conflicts.append((seen_times[task.time], (pet, task)))
            else:
                seen_times[task.time] = (pet, task)

        return conflicts