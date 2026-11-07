
# PawPal+ Smart Planner — Model Card

## 1. System Overview

PawPal+ Smart Planner is a Python-based pet-care scheduling application developed for CodePath AI110.

The project extends my original Module 2 application by adding a planning, verification, and explanation workflow.

The system helps owners organize daily pet-care tasks while considering priorities, scheduling conflicts, and available time.

## 2. AI and Technical Approach

The system uses rule-based planning and reliability verification.

The workflow consists of three stages:

1. Plan: Select tasks using priority and scheduling rules.
2. Verify: Check selected tasks for conflicts and budget violations.
3. Explain: Present the recommended schedule and reasons for skipped tasks.

The current version does not use a trained machine-learning model, a large language model, or an external AI API.

Its advanced feature is the integrated reliability and testing system.

## 3. Human-AI Collaboration

I used an AI coding assistant to help understand Python concepts, develop the Smart Planner component, improve documentation, and design automated tests.

I reviewed the suggestions, ran the code in my own environment, and checked the results.

### Suggestion Accepted

I accepted the suggestion to add a separate SmartPlanner class that verifies scheduling results instead of replacing my original scheduling system.

This allowed me to reuse working code and add verification without changing the original application logic.

### Suggestion Revised

An early suggestion described the new workflow as agentic AI. However, the implementation uses deterministic scheduling rules rather than an autonomous AI agent.

I revised the technical description to accurately explain that the system uses rule-based planning and verification, not a generative AI model.

## 4. Reliability Testing

The original PawPal+ application passed 14 automated tests.

I added three additional Smart Planner tests:

1. Valid schedule verification.
2. Scheduling conflict handling.
3. Daily time-budget enforcement.

The combined test suite passed 17 tests during development.

I also manually tested overlapping tasks using the Streamlit application.

### Observed Result

Bella's Morning Walk:
- Start time: 08:00
- Duration: 30 minutes
- Priority: High

Luna's Breakfast:
- Start time: 08:15
- Duration: 15 minutes
- Priority: Medium

Result:
- Verification PASSED.
- Bella's Morning Walk was selected.
- Luna's Breakfast was skipped because of a scheduling conflict.
- Total scheduled time was 30 minutes.

## 5. Guardrails and Safety

The system includes:

- Validation of task information.
- Priority validation.
- Time-format validation.
- Prevention of overlapping selected tasks.
- Daily time-budget verification.
- Logging of planning activity.
- Explanations for skipped activities.

These checks help identify invalid inputs and scheduling issues.

## 6. Potential Biases and Risks

The planner prioritizes tasks marked as high priority.

This may cause lower-priority tasks to be skipped repeatedly.

The system relies on owners to enter appropriate priorities, durations, and schedules.

A skipped pet-care activity may still be important for an animal's well-being.

The planner should support human decision-making rather than replace the pet owner's judgment.

## 7. Limitations

- Tasks are not automatically rescheduled.
- The planner does not guarantee an optimal schedule.
- It does not understand individual animal medical needs.
- Task priorities are manually assigned.
- Data is not stored in a permanent database.
- The system does not use generative AI.
- More edge-case and long-term testing would improve reliability.

## 8. Human-in-the-Loop

Pet owners remain responsible for reviewing the recommended schedule.

They can adjust priorities, task times, and activity durations.

The application does not automatically execute pet-care activities or make irreversible decisions.

## 9. Future Improvements

Possible improvements include:

- Automatic conflict-free rescheduling.
- Persistent database storage.
- More comprehensive automated testing.
- Personalized planning based on pet requirements.
- Optional AI-assisted natural-language explanations.

## 10. Reflection

This project helped me understand how to extend an existing Python application into a more reliable software system.

I learned the importance of testing, validation, modular design, and explaining technical decisions.

Working with AI assistance also taught me to verify generated code and describe system capabilities accurately instead of assuming every suggestion is correct.

## 11. Responsible Use

PawPal+ Smart Planner is an educational software project.

It should not replace professional veterinary advice or the owner's responsibility to provide appropriate animal care.
