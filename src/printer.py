def print_output(pairs):
    for employee1, employee2, overlap_count in pairs:
        print(f'{employee1.name}-{employee2.name}: {overlap_count}')
