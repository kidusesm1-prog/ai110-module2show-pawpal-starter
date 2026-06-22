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
        new_pet = Pet(pet_name, species, age)
        owner.add_pet(new_pet)
        st.success(f"Added {pet_name}!")

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
            for pet in owner.pets:
                if pet.name == selected_pet:
                    pet.add_task(Task(description, time, frequency))
                    st.success(f"Added task for {selected_pet}!")
else:
    st.info("Add a pet first before scheduling tasks.")

st.header("Today's Schedule")

tasks = scheduler.get_today_schedule()
sorted_tasks = scheduler.sort_by_time(tasks)

if sorted_tasks:
    for pet, task in sorted_tasks:
        status = "Done" if task.completed else "Pending"
        st.write(f"**{task.time}** | {pet.name} | {task.description} | {task.frequency} | {status}")
else:
    st.write("No tasks scheduled yet.")