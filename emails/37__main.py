
def find_best_running_time(running_times):
    # Start with a really high number, this would be over 16 minutes.
    best_running_time = 1000
    for running_time in running_times:
        if running_time < best_running_time:
            best_running_time = running_time

    return best_running_time


def find_worst_running_time(running_times):
    # Start with an impossibly low number.
    worst_running_time = 0
    for running_time in running_times:
        if running_time > worst_running_time:
            worst_running_time = running_time

    return worst_running_time


running_times = [10.1, 9.5, 11.2, 8.5, 10.5]

best_running_time = find_best_running_time(running_times)
worst_running_time = find_worst_running_time(running_times)

print(f"My best running time is {best_running_time} minutes.")  # My best running time is 8.5 minutes.
print(f"My worst running time is {worst_running_time} minutes.")  # My worst running time is 11.2 minutes.


running_times = [10.1, 9.5, 11.2, 8.5, 10.5]

best_running_time = min(running_times)
worst_running_time = max(running_times)

print(f"My best running time is {best_running_time} minutes.")  # My best running time is 8.5 minutes.
print(f"My worst running time is {worst_running_time} minutes.")  # My worst running time is 11.2 minutes.
