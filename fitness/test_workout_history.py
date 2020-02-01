import datetime

import fitness.workout_history as workout_history

str_today = '2019-12-05 12:13:14'
str_1_day_ago = '2019-12-04 12:13:14'
str_2_days_ago = '2019-12-03 12:13:14'
str_3_days_ago = '2019-12-04 12:13:14'

today_datetime = datetime.datetime(2019, 12, 5, 12, 13, 14)
today_date = today_datetime.date()

workout_today = {'total_score': 11, 'finished_at': str_today, 'completed': True, 'workout': 'workout_1'}
workout_1_day_ago = {'total_score': 13, 'finished_at': str_1_day_ago, 'completed': True, 'workout': 'workout_1'}
workout_2_days_ago = {'total_score': 17, 'finished_at': str_2_days_ago, 'completed': True, 'workout': 'workout_2'}
workout_3_days_ago = {'total_score': 23, 'finished_at': str_3_days_ago, 'completed': False, 'workout': 'workout_2'}

expected_report_total = {
    "workouts_completed": 3,
    "total_score": 11 + 13 + 17,
    "days_in_a_row": 3,
    "by_workout": {
        "workout_1": {
            "completed": 2,
            "total_score": 11 + 13,
            "max_score": 13
        },
        "workout_2": {
            "completed": 1,
            "total_score": 17,
            "max_score": 17
        }
    }
}


def test_datetime_to_str():
    assert today_datetime == workout_history.str_to_datetime(str_today)


def test_get_completed_workouts():
    workouts = [workout_1_day_ago, workout_2_days_ago, workout_3_days_ago]
    workouts_completed = [workout_1_day_ago, workout_2_days_ago]

    # sanity: test case actually hands in at least 1 non-completed workout
    assert any([not w['completed'] for w in workouts])

    # actual test case of functionality
    assert workouts_completed == workout_history.get_completed_workouts(workouts)


def test_days_in_a_row__zero_days():
    workouts = [workout_2_days_ago]
    assert workout_history.days_in_a_row(workouts, today_date) == 0


def test_days_in_a_row__2_days():
    workouts = [workout_1_day_ago, workout_2_days_ago]
    assert workout_history.days_in_a_row(workouts, today_date) == 2


def test_days_in_a_row__include_today():
    workouts = [workout_today, workout_1_day_ago, workout_2_days_ago]
    assert workout_history.days_in_a_row(workouts, today_date) == 3


def test_by_workout():
    workouts = [workout_today, workout_1_day_ago, workout_2_days_ago]

    expected = {
        'workout_1': {
            'completed': 2,
            'total_score': 11 + 13,
            'max_score': 13
        },
        'workout_2': {
            'completed': 1,
            'total_score': 17,
            'max_score': 17
        }
    }

    assert workout_history.by_workout(workouts) == expected


def test_aggregate_workout_history():
    workouts = [workout_today, workout_1_day_ago, workout_2_days_ago, workout_3_days_ago]

    assert workout_history.aggregate_workout_history(workouts, today_date) == expected_report_total