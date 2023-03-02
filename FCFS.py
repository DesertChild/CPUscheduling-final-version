#implementation of CPU Scheduling Algorithms
#N0.1 FCFS
#use a FIFO Data Structure : queue ; insert from the head , empty from the tail
#need arrival time , burst time
from collections import deque, OrderedDict
import numpy as np
import sys

class Process:
    def __init__(self , name , a_time,b_time):
        self.name=name #a string : P1,P2 ,....
        self.a_time = a_time # an integer representing arrival time of the process
        self.b_time = b_time # an integer representing the burst time of the process , that is the total time taken by the process for its execution on the CPU

#the queue of the processes will be represented by the deque  from the collections

def firstComeFirstServed(queue,p_num):
    #display the info 
    print('the process chart')
    print("P  | A_time | B_time")
    for pro in queue:
        print(str(pro.name) +" | "+str(pro.a_time)+"      | "+str(pro.b_time))
    print()
    #gantt diagram
    tempo=0
    print('Gantt Diagram')
   
    for qu in queue:
        print(f' | P{qu.name} | {tempo}     {tempo+qu.b_time}')
        tempo+=qu.b_time
    print()
#compute waiting time for each process
    dict={}
    ref_time =0 #a helper in calculating the waiting time
    sum=0
    pr = queue.popleft()
    dict[pr.name]=str(0)
    ref_time = ref_time+pr.b_time
    for i in range(1,p_num):
        pr = queue.popleft()
        dict[pr.name]=str(ref_time-pr.a_time)
        ref_time=ref_time+pr.b_time
    for j in dict.values():
        sum+=int(j)
    
    return OrderedDict(sorted(dict.items())),(sum/len(dict))
#end of the function
if __name__ == '__main__':
    if len(sys.argv)!=2:
        print("Usage: FCFS.py <filename.txt>")
        quit()
    fil = sys.argv[1]
    matrix = np.loadtxt(str(fil), dtype='i', delimiter=',') #read from the file
    q=[]*len(matrix)
    for m in matrix:
        temp_proc=Process(name=m[0],a_time=m[1],b_time=m[2])
        q.append(temp_proc)
    
    #q=[Process(name=1,a_time=0,b_time=24),Process(name=2,a_time=0,b_time=3),Process(name=3,a_time=0,b_time=3)]
    queue=deque(q)
    result,average=firstComeFirstServed(queue,len(queue))
    print()
    print('|the waiting time chart|')
    print("P | Wait_Time")
    for process_id in result.keys():
        print(f'{process_id} | {result[process_id]}')
    
    print(f'average waiting time is : {average}')