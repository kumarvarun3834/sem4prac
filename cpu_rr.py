#id,BT,Priority
processes = [
    [1, 5, 2],
    [2, 3, 1],
    [3, 8, 4],
    [4, 6, 3]
]
def round_robin(processes,quantum):
    time = 0
    n = len(processes)
    burst_time = [p[1] for p in processes]
    remaining_bt = burst_time[:]
    waiting_time = [0] * n
    completion_time = [0] * n
    complete = 0
    while complete < n:
        done = True
        for i in range(n):
            if remaining_bt[i] > 0:
                done = False
                if remaining_bt[i] > quantum:
                    print(f'Process {processes[i][0]} {time} ---> {time + quantum}')
                    time += quantum
                    remaining_bt[i] -= quantum
                else:
                    print(f'Process {processes[i][0]} {time} ---> {time + remaining_bt[i]}')
                    time += remaining_bt[i]
                    waiting_time[i] = time - burst_time[i]
                    completion_time[i] = time
                    remaining_bt[i] = 0
                    complete += 1
        if done:
            break

    avg_wt = sum(waiting_time) / n
    avg_tat = sum(completion_time) / n

    print(f'average WT= {avg_wt}')
    print(f'average TAT= {avg_tat}')
round_robin(processes, quantum=2)