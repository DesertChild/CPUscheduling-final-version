#Implementation of CPU scheduling algorithms
#N0.4 Round Robin(it is preemptive)
#to calculate the waiting time for processes
#we're going to need, a list of processes and their relevant information
#and the quantum time of the CPU
import numpy as np
import sys

def roundRobin(processes,n, quantumTime):
    p=processes
    #display the info 
    print('|the process chart|')
    print("P  | A_time | B_time")
    for pro in p:
        print(str(pro[0]) +" | "+str(pro[1])+"      | "+str(pro[2]))
    print()
    w_t={}
    for i in range(n):
        w_t[p[i][0]] = 0
    ref_time=0
    finished= False
    counter=0
    #gnatt diagram here will be printed in pieces
    #on different lines of the program
    tempo=0
    print('|Gantt diagram|')
    #print(f'{tempo}',end=' ')
    #Gnatt end
    while(finished == False):
        for i in range(n):
            if(p[i][2]>0):
                if(p[i][2] > quantumTime):
                    #gnatt beginning
                    
                    print(f' |P{p[i][0]}| {tempo} {tempo+quantumTime}')
                    tempo+=quantumTime
                    #gnatt end
                    p[i][2] = p[i][2] - quantumTime
                    w_t[p[i][0]] += (ref_time-p[i][1])
                    ref_time +=quantumTime
                    p[i][1] = ref_time
                else: #that is if p[i][2]<= quantumTime
                    #gnatt
                    
                    print(f' |P{p[i][0]}| {tempo} {tempo+p[i][2]}')
                    tempo+=p[i][2]
                    w_t[p[i][0]] += (ref_time-p[i][1])
                    ref_time+=p[i][2]
                    p[i][2]=0
            if(p[i][2]==0):
                counter+=1
            if(counter==n):
                finished=True
    #gnatt beginning
    for pu in p:
        if pu[2]!=0:
            print(f' |P{pu[0]}| {tempo} {tempo+pu[2]}')
            tempo+=pu[2]
    print()
    #Gnatt end
    return w_t
#end of waiting time function
def averageWaitingTime(w):
    sum=0
    for i in w.values():
        sum+=int(i)
    return sum/len(w)
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: RR.py <filename.txt> quantum')
        quit()
    fil = sys.argv[1]
    quantum = int(sys.argv[2])
    pr = np.loadtxt(fil, dtype='i', delimiter=',')
    ww = roundRobin(pr,len(pr),quantum)
    average=averageWaitingTime(ww)
    print(f'the average waiting time is {average} seconds')