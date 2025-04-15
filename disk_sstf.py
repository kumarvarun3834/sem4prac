queue=[82,91,220,129,100,69]
head_start=45
def sstf(queue,start):
    reqs=queue[:]
    head=start
    total_moment=0
    sequence=[]
    while reqs:
        closest=reqs[0]
        min_distance=abs(closest-head)
        for i in range(1,len(reqs)):
            distance=abs(reqs[i]-head)
            if(distance<min_distance):
                closest=reqs[i]
                min_distance=distance
        total_moment+=abs(closest-head)
        sequence.append(closest)
        head=closest
        reqs.remove(closest)
    print('seek time ',total_moment)
    print('sequence ', sequence)
sstf(queue,head_start)