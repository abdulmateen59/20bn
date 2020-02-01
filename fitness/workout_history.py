import datetime
import itertools



def str_to_datetime(datetime_str):
    return datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')


def get_completed_workouts(workouts):
    #return [i for i in workouts if (i['completed'] == True)] 
    return  list(filter(lambda i: i['completed'] == True , workouts)) 


def days_in_a_row(completed_workouts, today):
    days_in_a_row = 0
    yesterday = today - datetime.timedelta(days=1) 
    for i in range(len(completed_workouts)):
        dt = str_to_datetime(completed_workouts[i]['finished_at']).date()
        if(days_in_a_row >= 1):
            if(abs((pre_dt - dt).days) == 1 or abs((pre_dt - dt).days) == 0):
                #print('Streak +1...')
                days_in_a_row += 1
            else:
                #print('Streak Revoked...')
                days_in_a_row = 0

        elif dt != today and dt != yesterday:
            days_in_a_row = 0
            #print('Streak Revoked...')

        elif dt == today or dt == yesterday:
            days_in_a_row = 1
            #print('Streak Started...')

        pre_dt = dt
    return days_in_a_row


def by_workout(completed_workouts):
    dict = {}
    for key, value in itertools.groupby(completed_workouts, key=lambda x:x['workout']):
        completed , total_score , max_score = 0 , 0 , 0
        for i in (list(value)):
            if(i['workout']==key):
                completed += 1
                total_score += int(i['total_score']) 
                if int(i['total_score']) > max_score:
                    max_score = int(i['total_score'])

        dict.update({key : { 'completed': completed ,
                                'total_score': total_score ,
                                'max_score' : max_score  } })
    return dict


def aggregate_workout_history(workouts, today):
    expected_report_total = {}
    completed_workouts = get_completed_workouts(workouts)
    days_in_row = days_in_a_row(completed_workouts,today)
    total_score = sum(item['total_score'] for item in completed_workouts)
    expected_report_total.update({'workouts_completed' : len(completed_workouts),
                                    'total_score' : total_score,
                                    'days_in_a_row' : days_in_row,
                                    'by_workout' : by_workout(completed_workouts)
                                })
    return expected_report_total