#implementation of CPU scheduling algorithms
#N0.3 Priority Scheduling
#considering the processes is a list of lists, given to the function as a driver code
#each list inside the processes represents a process respectively, 
#index 0 --> name, index 1 --> arrival_time , index 2 --> Burst_time, index 3 --> priority
import numpy as np
import sys

def waitingTime(processes,n): #n being the number of processes
    print('the process chart')
    print("P  | A_time | B_time | Priority")
    for pro in processes:
        print(str(pro[0]) +"  | "+str(pro[1])+"      | "+str(pro[2])+"     | "+str(pro[3]))
    print()
    w_t={} # the P --> waitingTime dictionary to populate and return
    processes=list(processes)
    processes.sort(key = lambda p: p[3]) #sort based on priority
    ref_time=0
    sum=0
    w_t['P'+str(processes[0][0])] = 0 # the first process has waiting time equal to 0
    ref_time+=processes[0][2]
    for i in range(1,n):
        w_t['P'+str(processes[i][0])] = ref_time - processes[i][1]
        ref_time+=processes[i][2]
    #calculating the average
    for j in w_t.values():
        sum+=int(j)
    #gantt diagram
    tempo=0
    print('||Gantt Diagram||')
    for proc in processes:
        print(f'|P{proc[0]}| {tempo}     {tempo + proc[2]}')
        tempo+=proc[2]
    print("\n")
    #end of Gnatt
    return w_t,(sum/len(w_t))

if __name__ == '__main__':
    if len(sys.argv)!=2:
        print("Usage: PS.py <filename.txt>")
        quit()
    fil = sys.argv[1]
    pr = np.loadtxt(fil, dtype='i', delimiter=',') #read from the file
    waiting,average = waitingTime(pr,len(pr))
    print('::Waiting Times chart::')
    for p in waiting.keys():
        print(f'{p}  {waiting.get(p)}')

    print(f"average time is : {average}")