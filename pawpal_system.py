from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List, Tuple


@dataclass
class Task:
    description: str
    time: str
    frequency: str = "once"
    completed: bool = False
    due_date: date = field(default_factory=date.today)

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True

    def create_next_occurrence(self):
        """Create the next task if this task repeats."""
        if self.frequency == "daily":
            next_date = self.due_date + timedelta(days=1)
        elif self.frequency == "weekly":
            next_date = self.due_date + timedelta(weeks=1)
        else:
            return None

        return Task(
            description=self.description,
            time=self.time,
            frequency=self.frequency,
            completed=False,
            due_date=next_date
        )


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
        """Return all tasks in the system."""
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

    def filter_by_status(self, completed):
        """Filter tasks by completion status."""
        return [
            (pet, task)
            for pet, task in self.owner.get_all_tasks()
            if task.completed == completed
        ]

    def mark_task_complete(self, pet_name, task_description, task_time):
        """Mark a task complete and create the next occurrence if recurring."""
        for pet in self.owner.pets:
            if pet.name.lower() == pet_name.lower():
                for task in pet.tasks:
                    if task.description == task_description and task.time == task_time:
                        task.mark_complete()

                        next_task = task.create_next_occurrence()
                        if next_task:
                            pet.add_task(next_task)

                        return f"Completed task: {task.description}"

        return "Task not found."

    def detect_conflicts(self):
        """Detect tasks scheduled at the same time."""
        conflicts = []
        seen_times = {}

        for pet, task in self.owner.get_all_tasks():
            if task.time in seen_times:
                first_pet, first_task = seen_times[task.time]
                conflicts.append(
                    f"Conflict at {task.time}: "
                    f"{first_pet.name} has '{first_task.description}' and "
                    f"{pet.name} has '{task.description}'."
                )
            else:
                seen_times[task.time] = (pet, task)

        return conflicts