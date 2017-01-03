
process_queue = []
start_time = 0
total_wtime = 0
wtime_queue = []
finish_time = 0
turnAround_time = []


def calculateWaitingAndTurnaroundTime(start_time, process_queue, wtime_queue,finish_time,turnAround_time):
    start_time = process_queue[0][1]
    finish_time = process_queue[0][1]
    for index in range(number_of_processes):
        wtime_queue.append(start_time - process_queue[index][1])
        start_time += process_queue[index][2]
        finish_time += process_queue[index][2]
        turnAround_time.append(finish_time - process_queue[index][1])
def display(number_of_processes,process_queue,wtime_queue,total_wtime,turnAround_time):
    print 'ProcessName\tArrivalTime\tBurstTime'
    for index in range(number_of_processes):
        print process_queue[index][0],'\t\t',process_queue[index][1],'\t\t',process_queue[index][2]

    for index in range(len(wtime_queue)):
        print "Process ", process_queue[index][0]
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


print 'Enter the total no of processes: '
value = raw_input()
while not (value.isdigit()):
    print "INVALID input!!!\n"
    print 'Enter the total no of processes: '
    value = raw_input()
number_of_processes = int(value)

userInput(number_of_processes)

process_queue.sort(key = lambda process_queue:process_queue[2])

calculateWaitingAndTurnaroundTime(start_time, process_queue, wtime_queue,finish_time,turnAround_time)
display(number_of_processes, process_queue, wtime_queue, total_wtime, turnAround_time)
