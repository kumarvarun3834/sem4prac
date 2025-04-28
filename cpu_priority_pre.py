# id, BT, Priority, Arrival Time
processes = [
    [1, 5, 2, 0],
    [2, 3, 1, 1],
    [3, 8, 4, 2],
    [4, 6, 3, 3]
]
def priority_pre(processes):
    n = len(processes)
    remaining_time = [p[1] for p in processes]
    pids=[p[0] for p in processes]
    burst_time = [p[1] for p in processes]
    arrival_time = [p[3] for p in processes]
    priority = [p[2] for p in processes]

    process_sequal=[]

    completion_time = [0] * n
    waiting_time = [0] * n
    tat = [0] * n

    complete = 0
    time = 0

    while complete < n:
        highest_priority = -1
        index = -1
        for i in range(n):
            if arrival_time[i] <= time and remaining_time[i] > 0:
                if priority[i] > highest_priority:
                    highest_priority = priority[i]
                    index = i

        if index == -1:
            time += 1
            continue

        time += 1
        process_sequal.append(pids[index])
        remaining_time[index] -= 1

        if remaining_time[index] == 0:
            complete += 1
            completion_time[index] = time
            tat[index] = completion_time[index] - arrival_time[index]
            waiting_time[index] = tat[index] - burst_time[index]

    total_wt = sum(waiting_time)
    total_tat = sum(tat)
    print(f"runnig sequence= {process_sequal}")

    print("PID  BT  Priority  AT  CT  TAT  WT")
    for i in range(n):
        print(f"{processes[i][0]}    {burst_time[i]}     {priority[i]}      {arrival_time[i]}  {completion_time[i]}  {tat[i]}   {waiting_time[i]}")
    print(f"\nAverage Waiting Time: {total_wt / n}")
    print(f"Average Turnaround Time: {total_tat / n}")
priority_pre(processes)