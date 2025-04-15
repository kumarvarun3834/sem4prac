queue=[82,91,220,129,100,69]
head_start=45
def fcfs(queue,head_start):
    head_moment=abs(head_start-queue[0])
    for i in range(1,len(queue)):
        head_moment+=abs(queue[i]-queue[i-1])
    print(head_moment)
fcfs(queue,head_start)