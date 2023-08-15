from datetime import datetime


def parse_time(time_range):
    return [time_range[:2], *time_range[2:].split('-')]


def calculate_time_overlap(start1, end1, start2, end2):
    start1_time = datetime.strptime(start1, '%H:%M')
    end1_time = datetime.strptime(end1, '%H:%M')
    start2_time = datetime.strptime(start2, '%H:%M')
    end2_time = datetime.strptime(end2, '%H:%M')

    return (start1_time <= end2_time) and (end1_time >= start2_time)
