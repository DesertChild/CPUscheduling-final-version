#CPU scheduling Algorithms
#N0.2 SJF(shortest job first)
#which process arrives first is executed until it execution ends
#all the other processes that arrive in the meantime are added to the execution pool,
#then after the running process ends, the burst times of those in the pool are compared and
#the one that has the lowest burst time will execute first.

import numpy as np
import sys

class Process:
    def __init__(self,id,a_time,b_time):
        self.id = id
        self.a_time = a_time
        self.b_time = b_time
        self.completed=0
        self.w_time=0

def shortestJobFirst(processes,n):
    #display the info 
    print('the process chart')
    print("P  | A_time | B_time")
    for pro in processes:
        print(str(pro.id) +" | "+str(pro.a_time)+"      | "+str(pro.b_time))
    print()
    p=processes.copy()
    w_t={}
    sum=0
    completed=0
    ref_time=0
    p.sort(key=lambda x: x.a_time)
    p[0].w_time=0
    p[0].completed=1
    ref_time+=p[0].b_time
    p_ref=p[0]
    w_t[p[0].id] = p[0].w_time
    completed=completed+1
    queue=[]
    while(1):
        for i in range(1,n):
            if p[i].a_time <= ref_time and p[i].completed==0:
                queue.append(p[i])
        queue.sort(key= lambda x : x.b_time)
        for j in range(len(queue)):
            queue[j].w_time=ref_time-queue[j].a_time
            #queue[j].wait_t(w)
            w_t[queue[j].id] = queue[j].w_time
            queue[j].completed=1
            completed+=1
            ref_time+=queue[j].b_time
            for i in range(len(p)):
                if p[i].id == queue[j].id:
                    p[i].completed=1
            p_ref=queue[j]
            queue.clear()
            break
        if completed == n:
            break
    #gantt diagram
    tempo=0
    print('||Gantt Diagram||')
    for this_process in w_t.keys():
        for proc in p:
            if proc.id == this_process:
                print(f' |P{this_process}| {tempo} {tempo+(proc.b_time)}')
                tempo+=proc.b_time
                break
    print()
    #end of Gnatt
    for k in w_t.values():
        sum+=int(k)
    return w_t,sum/len(w_t)
#end of the ShortestJobFirst Function

if __name__ == '__main__':
    if len(sys.argv)!=2:
        print("Usage: SJF.py <filename.txt>")
        quit()
    fil = sys.argv[1]
    matrix = np.loadtxt(fil, dtype='i', delimiter=',') #read from the file
    pr=[]*len(matrix)
    for m in matrix:
        temp_proc=Process(id=m[0],a_time=m[1],b_time=m[2])
        pr.append(temp_proc)
    #pr=[Process(id=1,a_time=0,b_time=7),Process(id=2,a_time=2,b_time=4),Process(id=3,a_time=4,b_time=1),Process(id=4,a_time=5,b_time=4)]
    ww,average = shortestJobFirst(pr,len(pr))
    #print(ww)
    print(f'average waiting time is {average} seconds')