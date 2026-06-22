from pawpal_system import Owner, Pet, Task, Scheduler


def print_schedule(schedule):
    print("Today's Schedule")
    print("----------------")

    for pet, task in schedule:
        status = "Done" if task.completed else "Pending"
        print(f"{task.time} | {pet.name} | {task.description} | {task.frequency} | {status}")


owner = Owner("Kidus")

dog = Pet("Max", "Dog", 3)
cat = Pet("Luna", "Cat", 2)

dog.add_task(Task("Morning walk", "08:00", "daily"))
dog.add_task(Task("Vet appointment", "14:30", "once"))
cat.add_task(Task("Feed wet food", "07:30", "daily"))

owner.add_pet(dog)
owner.add_pet(cat)

scheduler = Scheduler(owner)

schedule = scheduler.get_today_schedule()
sorted_schedule = scheduler.sort_by_time(schedule)

print_schedule(sorted_schedule)