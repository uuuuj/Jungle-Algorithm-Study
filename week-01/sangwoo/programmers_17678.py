# https://school.programmers.co.kr/learn/courses/30/lessons/17678

def string_to_minute(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def minute_to_string(minute):
    h = minute // 60
    m = minute % 60
    
    string_h = f'0{h}' if h < 10 else f'{h}'
    string_m = f'0{m}' if m < 10 else f'{m}'
    
    return f'{string_h}:{string_m}'
    


def solution(n, t, m, timetable):
    answer = ''
    
    crew_time = sorted([ string_to_minute(time) for time in timetable ])
    
    bus_time = [ 540 + i * t for i in range(n) ]
    
    ride_index = 0
    
    
    for bt in bus_time:
        cnt = 0
        
        while ride_index < len(crew_time) and crew_time[ride_index] <= bt and cnt < m:
            ride_index += 1
            cnt += 1
    
    if cnt < m:
        return minute_to_string(bus_time[-1])
    
    else:
        return minute_to_string(crew_time[ride_index - 1] - 1)
    