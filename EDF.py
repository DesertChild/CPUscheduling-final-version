import math
import numpy as np
import sys

def LCM(l):
    cm = l[0]
    for i in range(1,len(l)):
        cm = cm*l[i]//math.gcd(cm, l[i])
    return cm

def earliestDeadlineFirst(pr,n):
    processes=list(pr)
    u=0
    for i in range(n): # the utilization factor for the algorithm to work must be < 1
        u+=processes[i][1]/processes[i][2]

    print("Utilization: ",u)
    if u>1:
        print("The utilization factor is not reliable!")

    else:

        temp_p=[]
        for i in range(n):
            temp_p.append(processes[i][2])
        lcm=LCM(temp_p)
        print(f'max reachable time is {lcm}')

        #calculating the time slots for each process
        i=0
        periods=[]
        for i in range(n):
            j=1
            while 1: #calculating and storing the time instances of the deadlines of the processes, defining the periods
                if j*processes[i][2]<=lcm:
                    periods.append([processes[i],j*processes[i][2]])
                    j+=1
                else:
                    break
        #end of time slot calculations
        for i in range(len(periods)): #get the next upcoming deadline less than the lcm of each process and storing them
            tmp = periods[i].copy() # copy in a new list to perform further calculations
            k = i
            while k > 0 and tmp[1] < periods[k-1][1]: #store an ordered list of upcoming deadlines
                periods[k] = periods[k - 1].copy()
                k -= 1
            periods[k] = tmp.copy()
        remainingTime=[]

        for i in range(n):
            if processes[i][4]==0:
                remainingTime.append(processes[i][1])
            else:
                remainingTime.append(0)


        timeLine=[]
        current_time=0 #start from zero go up to lcm that is the maximum reachable time
    
        while current_time<lcm:
            for i in range(n):
                if current_time>1 and ((current_time%processes[i][2]==0 and current_time>processes[i][4]) or current_time==processes[i][4]):
                    remainingTime[i]=processes[i][1] #populate the remaining time list with the amount of time remaining from the execution of the processes
            done=0
            for j in range(len(periods)):
                if j==0 and remainingTime[periods[j][0][0]-1]>0:
                    timeLine.append(periods[j][0][0])
                    remainingTime[periods[j][0][0]-1]-=1
                    done=1
                    if remainingTime[periods[j][0][0]-1]==0:
                        periods.pop(j)
                    break

                elif j>0 and periods[j][1]==periods[0][1]:
                    if remainingTime[periods[j][0][0]-1]>0:
                        tmp=periods[j].copy()
                        periods[j]=periods[0].copy()
                        periods[0]=tmp.copy()
                        current_time-=1
                        done=1
                        break
                elif j>0 and remainingTime[periods[j][0][0]-1]>0:
                    timeLine.append(periods[j][0][0])
                    remainingTime[periods[j][0][0]-1]-=1
                    done=1
                    if remainingTime[periods[j][0][0]-1]==0:
                        periods.pop(j)
                    break
                

            if done==0:
                timeLine.append(0)

            current_time+=1


        beginning_point=0
        ending_point=1
        #gnatt
        print('||Gantt diagram||')
        #print(int(0),end=' ')
        for i in range(lcm):
            if i>0 and timeLine[i]!=timeLine[i-1] and timeLine[i-1] != 0:
                ending_point=i
                print(f'| P{timeLine[i-1]} |  {beginning_point}     {ending_point}')
                beginning_point=i
            if i==lcm-1 and timeLine[i] != 0:
                ending_point=lcm
                print(f'| P{timeLine[i]} |  {beginning_point}     {ending_point}')

    
        for i in range(len(periods)):
            print(periods[i])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: EDF.py <filename.txt>')
        quit()

    fil= sys.argv[1]
    processes = np.loadtxt(fil, dtype='i', delimiter=',')
    print('the processes represented as lines of a matrix are as: ')
    print(processes)
    pr = list(processes)
    earliestDeadlineFirst(pr,len(processes))