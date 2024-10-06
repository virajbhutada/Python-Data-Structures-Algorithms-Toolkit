def activity_selection(start_times, end_times):
    activities = sorted(zip(start_times, end_times), key=lambda x: x[1])
    selected_activities = []

    last_end_time = -1
    for start, end in activities:
        if start > last_end_time:
            selected_activities.append((start, end))
            last_end_time = end

    return selected_activities

# Test
start_times = [1, 3, 0, 5, 8, 5]
end_times = [2, 4, 6, 7, 9, 9]
print(activity_selection(start_times, end_times))  # Output: [(1, 2), (3, 4), (5, 7), (8, 9)]
