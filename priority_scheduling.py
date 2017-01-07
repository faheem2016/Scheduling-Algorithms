
process_queue = []
start_time = 0
total_waiting_time = 0
waiting_time_queue = []
finish_time = 0
turn_around_time = []


def calculate_waiting_and_turnaround_time(start_time, process_queue, waiting_time_queue,finish_time,turn_around_time):
    start_time = process_queue[0][1]
    finish_time = process_queue[0][1]
    for index in range(number_of_processes):
        waiting_time_queue.append(start_time - process_queue[index][1])
        start_time += process_queue[index][2]
        finish_time += process_queue[index][2]
        turn_around_time.append(finish_time - process_queue[index][1])
def display(number_of_processes,process_queue,waiting_time_queue,total_waiting_time,turn_around_time):
    print 'ProcessName\tArrivalTime\tBurstTime'
    for index in range(number_of_processes):
        print process_queue[index][0],'\t\t',process_queue[index][1],'\t\t',process_queue[index][2]

    for index in range(len(waiting_time_queue)):
        print "Process ", process_queue[index][0]
        print "Waiting time ", waiting_time_queue[index]
        print 'Turnaround time: ', turn_around_time[index]
        total_waiting_time += waiting_time_queue[index]
        print "\n"

    print 'Total waiting time: ', total_waiting_time
    print 'Average waiting time: ',float(total_waiting_time/ number_of_processes)
def user_input(number_of_processes):
    for index in range(number_of_processes):
        process_queue.append([])  # append a list object to the list for every process
        process_queue[index].append(raw_input('Enter process name: '))
        value = raw_input('Enter process arrival time: ')
        while not (value.isdigit()):
            print "INVALID input!!!\n"
            value = raw_input('Enter process arrival time: ')
        process_queue[index].append(int(value))
        value = raw_input('Enter process burst time: ')
        while not (value.isdigit()):
            print "INVALID input!!!\n"
            value = raw_input('Enter process burst time: ')
        process_queue[index].append(int(value))
        value = raw_input('Enter process priority: ')
        while not (value.isdigit()):
            print "INVALID input!!!\n"
            value = raw_input('Enter process priority: ')
        process_queue[index].append(int(value))
        print '\n'

value = raw_input('Enter the total no of processes: ')
while not (value.isdigit()):
    print "INVALID input!!!\n"
    value = raw_input('Enter the total no of processes: ')
number_of_processes = int(value)
user_input(number_of_processes)

process_queue.sort(key = lambda process_queue:process_queue[3])

calculate_waiting_and_turnaround_time(start_time, process_queue, waiting_time_queue,finish_time,turn_around_time)
display(number_of_processes, process_queue, waiting_time_queue, total_waiting_time, turn_around_time)
