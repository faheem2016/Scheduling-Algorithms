import Queue

ready_queue = Queue.Queue()

process_queue = []
wtime_queue = []
turnAround_time = []
process_queue2 = []
completedProcesses = []

total_wtime = 0
finish_time = 0
current_running = 0

def getMinProcess(queue):
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
                minProcess = value
            queue.put(value)
        return minProcess
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

    print 'Total waiting time: ',total_wtime
    print 'Average waiting time: ',float(total_wtime/ number_of_processes)
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
def initialize():
    for index in range(number_of_processes):
        process_queue2.append([])
        process_queue2[index].append(process_queue[index][0])
        process_queue2[index].append(process_queue[index][1])
        process_queue2[index].append(process_queue[index][2])
        process_queue2[index].append(current_running)
        process_queue2[index].append(process_queue[index][2])
        process_queue2[index].append(finish_time)

    process_queue2.reverse()

    ready_queue.put(process_queue2.pop())
def calculateTimes():
    for index in range(number_of_processes):
        wtime_queue.append(completedProcesses[index][5] - completedProcesses[index][1] - completedProcesses[index][4])
        turnAround_time.append(completedProcesses[index][5] - completedProcesses[index][1])

print 'Enter the total no of processes: '
value = raw_input()
while not (value.isdigit()):
    print "INVALID input!!!\n"
    print 'Enter the total no of processes: '
    value = raw_input()
number_of_processes = int(value)

userInput(number_of_processes)

initialize()
current_procees = getMinProcess(ready_queue)
time_line = current_procees[1]
increment = 0
while increment < current_procees[4]:

    current_procees[3] += 1
    current_procees[2] -= 1
    time_line += 1

    if  current_procees[2] is 0:
        current_procees[5] = time_line
        completedProcesses.append(current_procees)

        popCompletedProcess(ready_queue)

        if getMinProcess(ready_queue) is None:
            break

        current_procees = getMinProcess(ready_queue)
        increment = current_procees[3]-1


    for i in range(len(process_queue2)):
        if time_line is process_queue2[i][1]:
            ready_queue.put(process_queue2[i])
            process_queue2.pop()
            ready_queue.put(current_procees)
            popCurrentProcess(current_procees, ready_queue)

            current_procees = getMinProcess(ready_queue)

            increment = -3
            break
    increment += 1

completedProcesses.sort(key = lambda completedProcesses:completedProcesses[1])

calculateTimes()


display(number_of_processes, completedProcesses, wtime_queue, total_wtime, turnAround_time)
