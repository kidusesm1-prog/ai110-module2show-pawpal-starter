import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.title("PawPal+")

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Pet Owner")

owner = st.session_state.owner
scheduler = Scheduler(owner)

st.header("Add a Pet")

with st.form("add_pet_form"):
    pet_name = st.text_input("Pet name")
    species = st.text_input("Species")
    age = st.number_input("Age", min_value=0, step=1)
    submitted_pet = st.form_submit_button("Add Pet")

    if submitted_pet:
        if pet_name.strip() and species.strip():
            owner.add_pet(Pet(pet_name, species, age))
            st.success(f"Added {pet_name}!")
        else:
            st.warning("Please enter a pet name and species.")

st.header("Schedule a Task")

pet_names = [pet.name for pet in owner.pets]

if pet_names:
    with st.form("add_task_form"):
        selected_pet = st.selectbox("Choose pet", pet_names)
        description = st.text_input("Task description")
        time = st.text_input("Time", placeholder="Example: 08:00")
        frequency = st.selectbox("Frequency", ["once", "daily", "weekly"])
        submitted_task = st.form_submit_button("Add Task")

        if submitted_task:
            if description.strip() and time.strip():
                for pet in owner.pets:
                    if pet.name == selected_pet:
                        pet.add_task(Task(description, time, frequency))
                        st.success(f"Added task for {selected_pet}!")
            else:
                st.warning("Please enter a task description and time.")
else:
    st.info("Add a pet first before scheduling tasks.")

st.header("Conflict Warnings")

conflicts = scheduler.detect_conflicts()

if conflicts:
    for conflict in conflicts:
        st.warning(conflict)
else:
    st.success("No scheduling conflicts found.")

st.header("Today's Schedule")

pet_filter = st.selectbox("Filter by pet", ["All"] + pet_names if pet_names else ["All"])
status_filter = st.selectbox("Filter by status", ["All", "Pending", "Done"])

tasks = scheduler.get_today_schedule()

if pet_filter != "All":
    tasks = scheduler.filter_by_pet(pet_filter)

if status_filter == "Pending":
    tasks = [(pet, task) for pet, task in tasks if not task.completed]
elif status_filter == "Done":
    tasks = [(pet, task) for pet, task in tasks if task.completed]

sorted_tasks = scheduler.sort_by_time(tasks)

if sorted_tasks:
    table_data = []

    for pet, task in sorted_tasks:
        table_data.append(
            {
                "Time": task.time,
                "Pet": pet.name,
                "Task": task.description,
                "Frequency": task.frequency,
                "Due Date": task.due_date,
                "Status": "Done" if task.completed else "Pending",
            }
        )

    st.table(table_data)

    st.subheader("Mark Tasks Complete")

    for index, (pet, task) in enumerate(sorted_tasks):
        if not task.completed:
            button_label = f"Mark complete: {pet.name} - {task.description} at {task.time}"

            if st.button(button_label, key=f"complete_{index}_{pet.name}_{task.description}_{task.time}_{task.due_date}"):
                message = scheduler.mark_task_complete(pet.name, task.description, task.time)
                st.success(message)
                st.rerun()
else:
    st.write("No tasks scheduled yet.")