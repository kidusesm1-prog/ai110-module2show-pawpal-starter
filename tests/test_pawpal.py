from pawpal_system import Pet, Task


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