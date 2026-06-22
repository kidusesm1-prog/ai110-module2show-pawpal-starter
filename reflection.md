# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

I chose four main classes: Owner, Pet, Task, and Scheduler. The Owner class manages the pets. The Pet class stores information about each pet and keeps track of that pet’s tasks. The Task class represents one care activity, such as feeding, walking, medication, or an appointment. The Scheduler class organizes all tasks across the owner’s pets and will later handle sorting, filtering, recurring tasks, and conflict detection.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

At this stage, my design is still simple. I kept the classes focused on the main requirements and avoided adding extra features too early. I may update the design later after implementing the scheduling logic.

The three core actions a user should be able to perform are:

1. Add a pet with basic information like name, species, and age.
2. Schedule care tasks for a pet, such as feeding, walking, medication, or appointments.
3. View today’s tasks in an organized schedule so the owner knows what needs to be done.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
