#CPU scheduling Algorithms
#N0.5 SRTF(shortest remaining time first)(preemptive SJF)
import numpy as np
import sys

def ShortestRemainingTime(processes,n):
    #list
    processes=list(processes)
    #display the info 
    print('the process chart')
    print("P  | A_time | B_time")
    for pro in processes:
        print(str(pro[0]) +" | "+str(pro[1])+"      | "+str(pro[2]))
    print()
    max_time=0
    for k in processes: #used for gnatt diagram
        max_time +=k[2]
    max = 0 #use max and minimum are used as a reference for updating the minimum time process
    remaining_time=[0]*n
    w_time  = {} #used in order to store the waiting times
                    #of the processes in corresponding indexes
    current_time=0
    p=processes
    p.sort(key= lambda x:x[1]) #sort the processes based on the arrival time
    for j in range(n):
        remaining_time[j] = p[j][2]
        if p[j][2]>max:
            max=(p[j][2]+1)
    minimum=1000000
    current_process=p[0] #take the process that arrives first to start executing now
    current_index = p.index(current_process)
    finished =0 #number of processes whose execution is completed
    changed = 0 #set to 0: the process is not replaced, set to :1 the process is replaced
    #gantt
    print('|Gantt Diagram|')
    tempo0=0
    tempo1=list()
    while(finished!=n):
        for i in range(n):
            if((p[i][1]<= current_time) and (remaining_time[i]<minimum) and(remaining_time[i]>0)):
                tempo1.append([current_index+1,tempo0,current_time])
                tempo0=current_time
                minimum = remaining_time[i]
                current_index=i
                changed=1
        if(changed ==0):
            current_time+=1
            continue
        #gnatt
        remaining_time[current_index] -=1
        minimum =remaining_time[current_index]
        if(minimum==0):
            minimum=max
        if(remaining_time[current_index] ==0):
            w_time[current_index] = ((current_time+1) - p[current_index][1]-p[current_index][2])
            finished+=1
            changed=0 # the process gets reset; in a way starting from a new process in the next cycle
            
        current_time +=1
    #gantt
    tempo1.append([current_index+1,tempo0,current_time])
    for gn in tempo1:
        if gn[1]!=gn[2]:
            print(f'P{gn[0]}  {gn[1]}  {gn[2]}')
    print()
    return w_time

def averageWaitingTime(wait_times):
    sum=0
    for i in wait_times.values():
        sum+=i
    return sum/len(wait_times)

if __name__ == '__main__':
    if len(sys.argv)!=2:
        print("Usage: SRTF.py <filename.txt>")
        quit()
    pr = np.loadtxt("SRTFprocesses.txt", dtype='i', delimiter=',')
    w=ShortestRemainingTime(pr,len(pr))
    print(f'average waiting time is {averageWaitingTime(w)} seconds')