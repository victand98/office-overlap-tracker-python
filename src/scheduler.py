def calculate_overlap(schedule1, schedule2):
    overlap_count = 0

    for period1 in schedule1:
        day1, start1, end1 = period1
        for period2 in schedule2:
            day2, start2, end2 = period2

            if day1 == day2:
                if (start1 <= end2) and (end1 >= start2):
                    overlap_count += 1

    return overlap_count
