#id,BT,Priority
processes = [
    [1, 5, 2],
    [2, 3, 1],
    [3, 8, 4],
    [4, 6, 3]
]
def priority(processes):
    time=0
    n=len(processes)
    waiting_time=0
    completion_time=0
    process_sequal=[]
    completed=[False]*n
    for i in range(len(processes)):
        for j in range(0,n-i-1):
            if processes[j][2]>processes[j+1][2]:
                processes[j],processes[j+1]=processes[j+1],processes[j]

    for i in range(len(processes)):
        print(f'Process {processes[i][0]} {time} -->')
        completion_time+=processes[i][1]
        process_sequal.append(processes[i][0])
        waiting_time=completion_time-processes[i][1]
        time+=processes[i][1]
        print(f'{time}')
        completed[i]==True
    print(f'average WT= {waiting_time/n}')
    print(f'average TAT= {completion_time/n}')
    print(f"runnig sequence= {process_sequal}")
priority(processes)