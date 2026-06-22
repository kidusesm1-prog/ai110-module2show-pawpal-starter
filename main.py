from pawpal_system import Owner, Pet, Task, Scheduler


def print_schedule(title, schedule):
    print(title)
    print("-" * len(title))

    for pet, task in schedule:
        status = "Done" if task.completed else "Pending"
        print(
            f"{task.time} | {pet.name} | {task.description} | "
            f"{task.frequency} | {task.due_date} | {status}"
        )

    print()


owner = Owner("Kidus")

dog = Pet("Max", "Dog", 3)
cat = Pet("Luna", "Cat", 2)

dog.add_task(Task("Vet appointment", "14:30", "once"))
dog.add_task(Task("Morning walk", "08:00", "daily"))
cat.add_task(Task("Feed wet food", "07:30", "daily"))
cat.add_task(Task("Medication", "08:00", "daily"))

owner.add_pet(dog)
owner.add_pet(cat)

scheduler = Scheduler(owner)

all_tasks = scheduler.get_today_schedule()
sorted_tasks = scheduler.sort_by_time(all_tasks)

print_schedule("Today's Schedule Sorted by Time", sorted_tasks)

max_tasks = scheduler.filter_by_pet("Max")
print_schedule("Filtered Tasks for Max", max_tasks)

pending_tasks = scheduler.filter_by_status(False)
print_schedule("Pending Tasks", pending_tasks)

print("Conflict Warnings")
print("-----------------")
for conflict in scheduler.detect_conflicts():
    print(conflict)

print()

print(scheduler.mark_task_complete("Max", "Morning walk", "08:00"))

updated_tasks = scheduler.sort_by_time(scheduler.get_today_schedule())
print_schedule("Updated Schedule After Completing Recurring Task", updated_tasks)