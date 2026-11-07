
# PawPal+ Smart Planner
## CodePath AI110 — Applied AI System Final Project

### Project Summary

PawPal+ Smart Planner is a Python and Streamlit application that helps pet owners organize daily care activities. It prioritizes tasks, detects overlapping schedules, respects daily time limits, and explains scheduling decisions.

This project extends my original Module 2 PawPal+ application with a reliability and verification workflow.

### Original Project — Module 2

My original project was PawPal+, a pet-care management system built with Python and Streamlit. It allowed owners to register pets, schedule activities, set priorities, identify conflicts, and manage recurring tasks.

The original system used object-oriented Python classes: Owner, Pet, Task, and Scheduler.

### New Features

- Verified Smart Planner
- Priority-based scheduling
- Conflict detection
- Daily time-budget verification
- Explanations for skipped tasks
- Application logging
- Automated reliability testing
- Streamlit user interface

### Advanced Feature: Reliability and Verification

The system uses a Plan, Verify, Explain workflow.

1. PLAN: The Scheduler creates a daily schedule using task priorities and available time.
2. VERIFY: The Smart Planner independently checks the selected schedule for overlaps and budget violations.
3. EXPLAIN: The application displays the selected tasks, skipped tasks, and verification results.

This system uses transparent rule-based planning. It does not use a generative language model, RAG, or an external AI API.

### System Architecture

The application consists of:

- app.py — Streamlit user interface
- pawpal_system.py — Pet, Owner, Task, and Scheduler classes
- smart_planner.py — Planning verification and explanation
- test_smart_planner.py — Reliability tests

The architecture diagram is saved in:

`diagrams/architecture.mmd`

### Setup Instructions

Requirements:
- Python 3.10 or newer
- pip
- Git

Clone the repository:

```bash
git clone https://github.com/rinty2616/applied-ai-system-final.git
cd applied-ai-system-final
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pytest
```

Run the application:

```bash
python -m streamlit run app.py
```

Open http://localhost:8501 in your browser.

### Sample Interactions

#### Example 1 — Scheduling Conflict

Input:

```text
Pet: Bella
Task: Morning Walk
Time: 08:00
Duration: 30 minutes
Priority: High

Pet: Luna
Task: Breakfast
Time: 08:15
Duration: 15 minutes
Priority: Medium
```

Observed output:

```text
Verification PASSED — 30 minutes scheduled.

Recommended schedule:
Bella: Morning Walk at 08:00 (high priority)

Skipped:
Luna's Breakfast overlaps Bella's Morning Walk.
```

#### Example 2 — No Scheduling Conflict

Input:

```text
Daily time budget: 60 minutes
Bella: Morning Walk, 08:00, 30 minutes
Luna: Breakfast, 09:00, 15 minutes
```

Expected output:

```text
Verification PASSED
Total scheduled minutes: 45
Both tasks selected
No skipped tasks
```

#### Example 3 — Insufficient Time Budget

Input:

```text
Daily time budget: 20 minutes
Bella: Morning Walk, 08:00, 30 minutes
```

Expected output:

```text
Verification PASSED
Total scheduled minutes: 0
Morning Walk skipped because it exceeds the time budget.
```

### Reliability Testing

The project uses pytest to test its scheduling and verification logic.

Run all tests:

```bash
python -m pytest -q
```

The original project passed 14 tests.

Three additional tests cover:

1. Valid schedule verification
2. Scheduling conflict handling
3. Daily time-budget enforcement

The combined suite passed 17 tests.

Test evidence is saved in:

- evidence/baseline_tests.txt
- evidence/smart_planner_tests.txt

### Design Decisions and Trade-offs

I reused the existing Scheduler to avoid duplicating scheduling logic.

I added independent verification to check that selected tasks satisfy basic scheduling constraints.

The planner follows a simple priority-based approach rather than a complex optimization algorithm. This makes its decisions easier to understand, but may not always produce the best possible schedule.

### Guardrails and Error Handling

- Task input validation
- Positive task-duration requirements
- Valid time formatting
- Priority validation
- Conflict prevention
- Daily time-budget checks
- Verification results
- Logging of planner activity

### Limitations

- The planner does not automatically move tasks to new times.
- It does not use a generative AI model.
- Data is stored in Streamlit session memory, not a permanent database.
- It does not guarantee the optimal schedule.
- Some unusual scheduling cases require additional testing.

### Testing Summary

The system successfully selected higher-priority tasks, skipped conflicting activities, and verified scheduled durations.

Further improvements could include automatic task rescheduling, persistent data storage, and more extensive reliability testing.

### Reflection

This project helped me understand how to extend an existing Python application into a more reliable system.

I practiced modular programming, verification, debugging, testing, and documenting technical decisions.

The detailed responsible-AI reflection and model limitations are documented separately in `model_card.md`.

### Project Repository

https://github.com/rinty2616/applied-ai-system-final

### Author

CodePath AI110 — Fall 2026

### Verified Example Outputs

Actual Smart Planner results from November 7, 2026:

```text
EXAMPLE 2: No scheduling conflict
{'date': '2026-11-07', 'verified': True, 'total_minutes': 45, 'schedule': ['Bella: Morning Walk at 08:00 (high priority)', 'Luna: Breakfast at 09:00 (medium priority)'], 'skipped': [], 'issues': []}

EXAMPLE 3: Insufficient time budget
{'date': '2026-11-07', 'verified': True, 'total_minutes': 0, 'schedule': [], 'skipped': ["Skipped Bella's 'Morning Walk': exceeds the 20-minute daily budget."], 'issues': []}
```
