# PawPal+

## Overview

PawPal+ is a smart pet care management system built with Python. The app helps pet owners organize daily care tasks such as feeding, walking, medication, and appointments.

This project uses object-oriented programming to model the main parts of the system: owners, pets, tasks, and a scheduler. The backend logic is built in `pawpal_system.py`, tested through a terminal demo in `main.py`, and connected to a Streamlit user interface in `app.py`.

## Core User Actions

A user should be able to:

1. Add a pet with basic information like name, species, and age.
2. Schedule care tasks for a pet, such as feeding, walking, medication, or appointments.
3. View an organized schedule so the owner knows what needs to be done.

## System Architecture

The system is built around four main classes:

* `Owner`: Stores and manages all pets.
* `Pet`: Stores pet details and that pet’s tasks.
* `Task`: Represents one care activity with a description, time, frequency, due date, and completion status.
* `Scheduler`: Organizes tasks across pets and handles sorting, filtering, recurring tasks, and conflict detection.

The UML diagrams are included in:

```text
diagrams/uml_draft.mmd
diagrams/uml_final.mmd
```

## Files

```text
pawpal_system.py          # Backend logic and main classes
main.py                  # CLI demo script
app.py                   # Streamlit user interface
tests/test_pawpal.py     # Automated pytest tests
diagrams/uml_draft.mmd   # Draft UML diagram
diagrams/uml_final.mmd   # Final UML diagram
reflection.md            # Project reflection
README.md                # Project documentation
```

## Running the CLI Demo

To run the terminal demo:

```bash
python main.py
```

## Sample CLI Output

```text
Today's Schedule Sorted by Time
-------------------------------
07:30 | Luna | Feed wet food | daily | 2026-06-23 | Pending
08:00 | Max | Morning walk | daily | 2026-06-23 | Pending
08:00 | Luna | Medication | daily | 2026-06-23 | Pending
14:30 | Max | Vet appointment | once | 2026-06-23 | Pending

Filtered Tasks for Max
----------------------
14:30 | Max | Vet appointment | once | 2026-06-23 | Pending
08:00 | Max | Morning walk | daily | 2026-06-23 | Pending

Pending Tasks
-------------
14:30 | Max | Vet appointment | once | 2026-06-23 | Pending
08:00 | Max | Morning walk | daily | 2026-06-23 | Pending
07:30 | Luna | Feed wet food | daily | 2026-06-23 | Pending
08:00 | Luna | Medication | daily | 2026-06-23 | Pending

Conflict Warnings
-----------------
Conflict at 08:00: Max has 'Morning walk' and Luna has 'Medication'.

Completed task: Morning walk

Updated Schedule After Completing Recurring Task
------------------------------------------------
07:30 | Luna | Feed wet food | daily | 2026-06-23 | Pending
08:00 | Max | Morning walk | daily | 2026-06-23 | Done
08:00 | Luna | Medication | daily | 2026-06-23 | Pending
08:00 | Max | Morning walk | daily | 2026-06-24 | Pending
14:30 | Max | Vet appointment | once | 2026-06-23 | Pending
```

## Running the Streamlit App

To run the browser app:

```bash
python -m streamlit run app.py
```

The Streamlit app allows the user to:

* Add pets
* Schedule tasks for pets
* View today’s schedule
* Filter tasks by pet
* Filter tasks by status
* See conflict warnings
* Mark tasks complete

The app uses `st.session_state` so pets and tasks stay available during the user’s current session.

## Smarter Scheduling

PawPal+ includes basic scheduling algorithms:

* `Scheduler.sort_by_time()` sorts all tasks in chronological order using the task time.
* `Scheduler.filter_by_pet()` filters tasks for one specific pet.
* `Scheduler.filter_by_status()` filters tasks based on whether they are complete or pending.
* `Scheduler.detect_conflicts()` checks if multiple tasks are scheduled at the same time and returns a warning.
* `Scheduler.mark_task_complete()` marks a task complete and creates the next task automatically for daily or weekly recurring tasks.

These features were tested in `main.py` using out-of-order tasks, duplicate task times, and a recurring daily task.

## Demo Walkthrough

A user can start by adding a pet, such as a dog named Max or a cat named Luna. After adding pets, the user can schedule tasks such as a morning walk, feeding, medication, or a vet appointment.

Once tasks are added, the scheduler organizes them by time so the schedule is easier to read. If two tasks are scheduled for the same time, the scheduler shows a conflict warning instead of crashing. If a daily or weekly recurring task is marked complete, the system creates the next occurrence automatically.

Example workflow:

```text
Add pet → Add task → View schedule → Detect conflicts → Mark recurring task complete
```

The main UI features are:

* Pet entry form
* Task entry form
* Schedule table
* Conflict warning area
* Filters for pet and task status
* Buttons for marking tasks complete

## Testing PawPal+

Tests can be run with:

```bash
python -m pytest
```

The automated tests verify:

* Task completion
* Adding tasks to pets
* Sorting tasks by time
* Recurring daily task creation
* Conflict detection for tasks scheduled at the same time

Example successful test output:

```text
5 passed
```

Confidence Level: ⭐⭐⭐⭐☆

The system handles the main required scheduling behaviors. More edge cases could be tested later, such as invalid time formats, pets with no tasks, or overlapping tasks with different start and end times.

## Reflection Summary

This project helped me practice designing a system before fully coding it. I started by planning the main classes with a UML diagram, then turned that design into Python code.

The biggest design choice was separating the system into `Owner`, `Pet`, `Task`, and `Scheduler`. This made the code easier to understand because each class has a clear job. The `Owner` manages pets, the `Pet` manages its tasks, the `Task` stores information about one care activity, and the `Scheduler` handles the logic across all pets.

One tradeoff I made was keeping conflict detection simple. The scheduler only checks for exact time matches, such as two tasks both scheduled at 08:00. This is easy to understand and test, but it does not detect overlapping tasks with different start and end times. For this project, that was a reasonable choice because each task only stores one time value.

AI was helpful for brainstorming the class structure, generating starter code, improving the scheduler logic, and creating tests. I still had to review the suggestions carefully and decide what fit the project requirements. Some AI ideas were too complex, so I kept the system focused on the main required features.

Overall, this project showed me that AI can help build faster, but I still need to act as the lead architect. I had to make design decisions, check the code, test the system, and make sure the final project stayed clear and usable.
