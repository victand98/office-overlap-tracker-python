from utils import parse_time


def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    data = {}
    for line in lines:
        name, schedule = line.strip().split('=')
        data[name] = [parse_time(slot) for slot in schedule.split(',')]

    return data
