Coding Exercise: Workout History
===

This is a coding exercise. Please follow the instructions to set up the project, 
complete the task and send your solution back to us.

**Time suggested**: We expect the time required to finish this exercise to be
around 2 hours.

## The task

We are working on a fitness product. This coding exercise covers an important
feature: Based on workouts from the past, we want to aggregate some basic 
metrics. These allow us to interact with the user in a meaningful way.

Example: The user has performed a workout 2 days in a row. We can use this
information to congratulate them and give motivation to keep building a habit.

Your task is to write a script that takes the history of workouts from the past
and produces an aggregation of the following metrics:

- How many days has the user performed workouts in a row? If they have neither
  performed a workout today or yesterday, their streak is broken and we start 
  counting again.
- Grouped by workout: How many points has the user accumulated over time, and
  what was their maximum score?
 
As a starting point, we provide you with the basic Python file structure and
unit test cases. In the beginning, these tests fail. Your task is to implement 
the missing functionality. 

**Note**: The unit tests are a guide to understand the interface of the 
functions. They may not test all possible cases, so you should not only add 
code to make the tests green, but actually implement functionality as it makes
sense.

## Setup

Check that you have Python 3 on your system. We're working on Python 3.6, but
any version of Python 3 should work for this exercise.

```shell script
python3 -V
# Python 3.6.9 (or similar output)
```

Navigate to task exercise

```shell script
cd /path/to/workout-history
```

Set up virtual environment.

```shell script
python3 -m venv ./env
``` 

Activate virtual environment.

```shell script
source env/bin/activate
```

Install requirements.

```shell script
pip install -r requirements.txt
```

Run unit tests. These will **fail** because the implementation is still missing.
This is intended at this point.

```
pytest
```

Now, it's your turn. Start adding code to `workout_history.py` and keep running
the unit tests. We have added docstrings that should explain the desired 
interface in enough detail. If in doubt, use your best judgement of what makes
sense. 
