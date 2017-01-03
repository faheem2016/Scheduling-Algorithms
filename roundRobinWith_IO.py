import Queue

ready_queue = Queue.Queue()
waiting_queue = Queue.Queue()

process_queue = []
wtime_queue = []
turnAround_time = []
process_queue2 = []
completedProcesses = []

total_wtime = 0
finish_time = 0
current_running = 0
last_time = -1
IO_Time = []
number_of_processes = 0
time_quantum = 0
IO_Type = 0
wait_time = 0

def getTopProcess(queue):
    if not queue.empty():
        flag = 0

        for i in range(queue.qsize()):
            value = queue.get()
            if  flag is 0:
                topProcess = value
                flag = 1
            queue.put(value)

        return topProcess
def popCompletedProcess(queue):
    if not queue.empty():
        time = []
        for i in range(queue.qsize()):
            value = queue.get()
            time.append(value[2])
            queue.put(value)

        minValueIndex = time.index(min(time))

        for index in range(queue.qsize()):
            value = queue.get()
            if minValueIndex is index:
                continue
            queue.put(value)
def popCurrentProcess(currentProcess, queue):
    if not queue.empty():

        flag = 0
        for i in range(queue.qsize()):
            value = queue.get()
            if flag is 0:
                if  current_procees[0] is value[0]:
                    flag = 1
                    continue

            queue.put(value)
def calculateTimes():
    completedProcesses.sort(key = lambda completedProcesses:completedProcesses[1])

    for index in range(number_of_processes):
        wtime_queue.append(completedProcesses[index][5] - completedProcesses[index][1] - completedProcesses[index][4])
        turnAround_time.append(completedProcesses[index][5] - completedProcesses[index][1])
def initialize():

    for index in range(number_of_processes):
        process_queue2.append([])
        process_queue2[index].append(process_queue[index][0])
        process_queue2[index].append(process_queue[index][1])
        process_queue2[index].append(process_queue[index][2])
        process_queue2[index].append(current_running)
        process_queue2[index].append(process_queue[index][2])
        process_queue2[index].append(finish_time)
        process_queue2[index].append(time_quantum)
        process_queue2[index].append(IO_Time[index])
        process_queue2[index].append(index+1) # process Number
        process_queue2[index].append(0)
        process_queue2[index].append(wait_time)

    for index in range(number_of_processes):
            if process_queue2[index][8] % 2 is 0:
                process_queue2[index].append(0)
            else:
                process_queue2[index].append(1)

    process_queue2.reverse()

    ready_queue.put(process_queue2.pop())

    process_queue2.sort(key = lambda process_queue2:process_queue2[1])
def makeProcessToComplete():
    current_procees[3] += 1
    current_procees[2] -= 1
    current_procees[6] -= 1
    current_procees[10] -= 1
def addToCompletedProcList():
    current_procees[5] = time_line
    completedProcesses.append(current_procees)

    popCompletedProcess(ready_queue)
def addNewProcToReadyQueue(flag):
    if ((time_line >= process_queue2[i][1]) and (last_time < process_queue2[i][1])):
        ready_queue.put(process_queue2[i])
        current_procees[6] = time_quantum
        flag = 1
        ready_queue.put(current_procees)
        popCurrentProcess(current_procees, ready_queue)
def display(number_of_processes,completedProcesses,wtime_queue,total_wtime,turnAround_time):
    print 'ProcessName\tArrivalTime\tBurstTime\tFinishTime'
    for index in range(number_of_processes):
        print completedProcesses[index][0],'\t\t\t', completedProcesses[index][1],'\t\t\t', completedProcesses[index][4],\
            '\t\t\t', completedProcesses[index][5]

    print "\n"

    for index in range(len(wtime_queue)):
        print "Process ", completedProcesses[index][0]
        print "Waiting time ", wtime_queue[index]
        print 'Turnaround time: ', turnAround_time[index]
        total_wtime += wtime_queue[index]
        print "\n"
def userInput(number_of_processes):
    for index in range(number_of_processes):
        process_queue.append([])  # append a list object to the list for every process
        process_queue[index].append(raw_input('Enter process name: '))
        print 'Enter process arrival time: '
        value = raw_input()
        while not (value.isdigit()):
            print "INVALID input!!!\n"
            print 'Enter process arrival time: '
            value = raw_input()
        process_queue[index].append(int(value))
        print 'Enter process burst time: '
        value = raw_input()
        while not (value.isdigit()):
            print "INVALID input!!!\n"
            print 'Enter process burst time: '
            value = raw_input()
        process_queue[index].append(int(value))
        print '\n'
def addProcessToWaitingQueue():
    flag = 0

    if current_procees[10] is 0:
        current_procees[10] = wait_time
        current_procees[9] = time_line + current_procees[7]
        waiting_queue.put(current_procees)
        for i in range(len(process_queue2)):
            if ((time_line >= process_queue2[i][1]) and (last_time < process_queue2[i][1])):
                ready_queue.put(process_queue2[i])
                flag = 1
        popCurrentProcess(current_procees, ready_queue)
    return flag

print 'Enter the total no of processes: '
value = raw_input()
while not (value.isdigit()):
    print "INVALID input!!!\n"
    print 'Enter the total no of processes: '
    value = raw_input()
number_of_processes = int(value)

print 'Enter the time Quantum: '
value = raw_input()
while not (value.isdigit()):
    print "INVALID input!!!\n"
    print 'Enter the time Quantum: '
    value = raw_input()
time_quantum = int(value)

print 'Enter the waiting time to perform I/O : '
value = raw_input()
while not (value.isdigit()):
    print "INVALID input!!!\n"
    print 'Enter the waiting time to perform I/O : '
    value = raw_input()
wait_time = int(value)

userInput(number_of_processes)

print "Press 1 for EVEN-PROCESS I/O \n"
print "Press 2 for ODD-PROCESS I/O \n"
choose = raw_input()
while not (choose.isdigit() and (int(choose) > 0 and int(choose) < 3)):
    print "INVALID input!!!\n"
    print "Press 1 for EVEN-PROCESS I/O \n"
    print "Press 2 for ODD-PROCESS I/O \n"
    choose = raw_input()
if int(choose) is 1:
    IO_Type = 0
else:
    IO_Type = 1

print "Press 1 to assign different I/O time for each process \n"
print "Press 2 to assign same I/O time for each process \n"
choose = raw_input()
while not (choose.isdigit() and (int(choose) > 0 and int(choose) < 3)):
    print "INVALID input!!!\n"
    print "Press 1 to assign different I/O time for each process \n"
    print "Press 2 to assign same I/O time for each process \n"
    choose = raw_input()

if int(choose) is 1:
    for index in range(number_of_processes):
        print "Enter process ", process_queue[index][0], " I/O time: "
        time = raw_input()
        while not (time.isdigit()):
            print "INVALID input!!!\n"
            print "Enter process ", process_queue[index][0], " I/O time: "
            time = raw_input()
        IO_Time.append(int(time))
elif int(choose) is 2:
    time = raw_input("Enter process I/O time: ")
    while not (time.isdigit()):
        print "INVALID input!!!\n"
        time = raw_input("Enter process I/O time: ")
    for index in range(number_of_processes):
        IO_Time.append(int(time))

initialize()
current_procees = getTopProcess(ready_queue)

time_line = current_procees[1]
increment = 0
while 1:
    time_line += 1
    if not ready_queue.qsize() is 0:
        makeProcessToComplete()

    if  current_procees[11] is IO_Type and current_procees[2] is not 0:
        flag = addProcessToWaitingQueue()
        if  flag is 1:
            last_time = time_line
    for index in range(waiting_queue.qsize()):
        process = waiting_queue.get()
        if process[9] is time_line:
            ready_queue.put(process)
            break
        else:
            waiting_queue.put(process)

    if  ready_queue.qsize() is 0:
        continue
    else:
        flag = 0
        for index in range(ready_queue.qsize()):
            process = ready_queue.get()

            if not current_procees[0] is process[0] and flag is not 1:
                current_procees = process
                flag = 1
            ready_queue.put(process)

    if  current_procees[2] is 0:

        addToCompletedProcList()

        for i in range(len(process_queue2)):
            if ((time_line >= process_queue2[i][1]) and (last_time < process_queue2[i][1])):
                ready_queue.put(process_queue2[i])
                last_time = time_line


        if len(completedProcesses) is number_of_processes:
            break

        if not ready_queue.qsize() is 0:
            current_procees = getTopProcess(ready_queue)

    if  current_procees[6] is 0:
        flag = 0
        for i in range(len(process_queue2)):
            addNewProcToReadyQueue(flag)

        if  flag is not 1:
            current_procees[6] = time_quantum
            ready_queue.put(current_procees)
            popCurrentProcess(current_procees, ready_queue)

        flag = 0
        last_time = time_line
        current_procees = getTopProcess(ready_queue)

calculateTimes()
display(number_of_processes, completedProcesses, wtime_queue, total_wtime, turnAround_time)
