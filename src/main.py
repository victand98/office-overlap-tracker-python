from employee import Employee
from scheduler import calculate_overlap
from reader import read_input
from printer import print_output

if __name__ == '__main__':
    input_data = read_input('input.txt')
    employees = [Employee(name, schedule)
                 for name, schedule in input_data.items()]

    pairs = []
    for i in range(len(employees)):
        for j in range(i + 1, len(employees)):
            employee1 = employees[i]
            employee2 = employees[j]
            overlap_count = calculate_overlap(
                employee1.schedule, employee2.schedule)
            pairs.append((employee1, employee2, overlap_count))

    print_output(pairs)
