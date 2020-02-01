#!/usr/bin/python
import fitness.workout_history as workout_history
import datetime

def main():
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

    print(workout_history.str_to_datetime(str_today))

    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<------------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
    workouts = [workout_1_day_ago, workout_2_days_ago, workout_3_days_ago]
    print(workout_history.get_completed_workouts(workouts))

    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<------------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
    print(workout_history.days_in_a_row([workout_2_days_ago] , today_date))
    print(workout_history.days_in_a_row([workout_1_day_ago, workout_2_days_ago] , today_date))
    print(workout_history.days_in_a_row([workout_today, workout_1_day_ago, workout_2_days_ago] , today_date)) 

    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<------------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
    workouts = [workout_today, workout_1_day_ago, workout_2_days_ago]
    print(workout_history.by_workout(workouts))

    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<------------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
    workouts = [workout_today, workout_1_day_ago, workout_2_days_ago, workout_3_days_ago]
    print(workout_history.aggregate_workout_history(workouts,today_date))


if __name__ == '__main__' :
    main()
