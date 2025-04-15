# id, BT, Priority, Arrival Time
processes = [
    [1, 5, 2, 0],
    [2, 3, 1, 1],
    [3, 8, 4, 2],
    [4, 6, 3, 3]
]

def sjrtf(processes):
    n = len(processes)
    burst_time = [p[1] for p in processes]
    arrival_time = [p[3] for p in processes]
    remaining_time = burst_time[:]
    completion_time = [0] * n
    waiting_time = [0] * n
    tat = [0] * n

    complete = 0
    time = 0
    prev_process = -1
    start_time = time

    while complete < n:
        shortest = -1
        min_bt = float('inf')

        for i in range(n):
            if arrival_time[i] <= time and remaining_time[i] > 0 and remaining_time[i] < min_bt:
                min_bt = remaining_time[i]
                shortest = i

        if shortest == -1:
            time += 1
            continue


        if shortest != prev_process:
            if prev_process != -1:
                print(f"Process {processes[prev_process][0]} {start_time} ---> {time}")
            start_time = time
            prev_process = shortest

        remaining_time[shortest] -= 1
        time += 1

        if remaining_time[shortest] == 0:
            complete += 1
            completion_time[shortest] = time
            tat[shortest] = completion_time[shortest] - arrival_time[shortest]
            waiting_time[shortest] = tat[shortest] - burst_time[shortest]


    if prev_process != -1:
        print(f"Process {processes[prev_process][0]} {start_time} ---> {time}")

    avg_wt = sum(waiting_time) / n
    avg_tat = sum(tat) / n

    print(f"\nAverage Waiting Time: {avg_wt}")
    print(f"Average Turnaround Time: {avg_tat}")

sjrtf(processes)
