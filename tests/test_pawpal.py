from datetime import date, timedelta

from pawpal_system import Owner, Pet, Task, Scheduler


def test_task_completion():
    task = Task("Morning walk", "08:00", "daily")

    task.mark_complete()

    assert task.completed is True


def test_task_addition():
    pet = Pet("Max", "Dog", 3)
    task = Task("Feed breakfast", "07:30", "daily")

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0].description == "Feed breakfast"


def test_sorting_correctness():
    owner = Owner("Kidus")
    pet = Pet("Max", "Dog", 3)

    pet.add_task(Task("Afternoon walk", "15:00", "once"))
    pet.add_task(Task("Breakfast", "07:30", "daily"))
    pet.add_task(Task("Medication", "09:00", "daily"))

    owner.add_pet(pet)
    scheduler = Scheduler(owner)

    sorted_tasks = scheduler.sort_by_time(scheduler.get_today_schedule())

    assert sorted_tasks[0][1].time == "07:30"
    assert sorted_tasks[1][1].time == "09:00"
    assert sorted_tasks[2][1].time == "15:00"


def test_recurring_task_creates_next_occurrence():
    owner = Owner("Kidus")
    pet = Pet("Max", "Dog", 3)

    task = Task("Morning walk", "08:00", "daily", due_date=date.today())
    pet.add_task(task)

    owner.add_pet(pet)
    scheduler = Scheduler(owner)

    scheduler.mark_task_complete("Max", "Morning walk", "08:00")

    assert len(pet.tasks) == 2
    assert pet.tasks[0].completed is True
    assert pet.tasks[1].completed is False
    assert pet.tasks[1].due_date == date.today() + timedelta(days=1)


def test_conflict_detection():
    owner = Owner("Kidus")

    dog = Pet("Max", "Dog", 3)
    cat = Pet("Luna", "Cat", 2)

    dog.add_task(Task("Morning walk", "08:00", "daily"))
    cat.add_task(Task("Medication", "08:00", "daily"))

    owner.add_pet(dog)
    owner.add_pet(cat)

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1
    assert "Conflict at 08:00" in conflicts[0]