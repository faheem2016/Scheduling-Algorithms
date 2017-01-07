import Queue

ready_queue = Queue.Queue()
waiting_queue = Queue.Queue()

process_queue = []
waiting_time_queue = []
turn_around_time = []
process_queue2 = []
completed_processes = []

total_waiting_time = 0
finish_time = 0
current_running = 0
last_time = -1
IO_Time = []
number_of_processes = 0
time_quantum = 0
IO_Type = 0
wait_time = 0

def get_top_process(queue):
    if not queue.empty():
        flag = 0

        for i in range(queue.qsize()):
            value = queue.get()
            if  flag is 0:
                top_process = value
                flag = 1
            queue.put(value)

        return top_process
def pop_completed_process(queue):
    if not queue.empty():
        time = []
        for i in range(queue.qsize()):
            value = queue.get()
            time.append(value[2])
            queue.put(value)

            min_value_index = time.index(min(time))

        for index in range(queue.qsize()):
            value = queue.get()
            if min_value_index is index:
                continue
            queue.put(value)
def pop_current_process(current_procees, queue):
    if not queue.empty():

        flag = 0
        for i in range(queue.qsize()):
            value = queue.get()
            if flag is 0:
                if  current_procees[0] is value[0]:
                    flag = 1
                    continue

            queue.put(value)
def calculate_times():
    completed_processes.sort(key = lambda completed_processes:completed_processes[1])

    for index in range(number_of_processes):
        waiting_time_queue.append(completed_processes[index][5] - completed_processes[index][1] - completed_processes[index][4])
        turn_around_time.append(completed_processes[index][5] - completed_processes[index][1])
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
def make_process_to_complete():
    current_procees[3] += 1
    current_procees[2] -= 1
    current_procees[6] -= 1
    current_procees[10] -= 1
def add_to_completed_process_List():
    current_procees[5] = time_line
    completed_processes.append(current_procees)

    pop_completed_process(ready_queue)
def add_new_process_to_ready_queue(flag):
    if ((time_line >= process_queue2[i][1]) and (last_time < process_queue2[i][1])):
        ready_queue.put(process_queue2[i])
        current_procees[6] = time_quantum
        flag = 1
        ready_queue.put(current_procees)
        pop_current_process(current_procees, ready_queue)
def display(number_of_processes,completed_processes,waiting_time_queue,total_waiting_time,turn_around_time):
    print 'ProcessName\tArrivalTime\tBurstTime\tFinishTime'
    for index in range(number_of_processes):
        print completed_processes[index][0],'\t\t\t', completed_processes[index][1],'\t\t\t', completed_processes[index][4],\
            '\t\t\t', completed_processes[index][5]

    print "\n"

    for index in range(len(waiting_time_queue)):
        print "Process ", completed_processes[index][0]
        print "Waiting time ", waiting_time_queue[index]
        print 'Turnaround time: ', turn_around_time[index]
        total_waiting_time += waiting_time_queue[index]
        print "\n"
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
        print '\n'
def add_process_to_waiting_queue():
    flag = 0

    if current_procees[10] is 0:
        current_procees[10] = wait_time
        current_procees[9] = time_line + current_procees[7]
        waiting_queue.put(current_procees)
        for i in range(len(process_queue2)):
            if ((time_line >= process_queue2[i][1]) and (last_time < process_queue2[i][1])):
                ready_queue.put(process_queue2[i])
                flag = 1
        pop_current_process(current_procees, ready_queue)
    return flag

value = raw_input('Enter the total no of processes: ')
while not (value.isdigit()):
    print "INVALID input!!!\n"
    value = raw_input('Enter the total no of processes: ')
number_of_processes = int(value)

value = raw_input('Enter the time Quantum: ')
while not (value.isdigit()):
    print "INVALID input!!!\n"
    value = raw_input('Enter the time Quantum: ')
time_quantum = int(value)

value = raw_input('Enter the waiting time to perform I/O : ')
while not (value.isdigit()):
    print "INVALID input!!!\n"
    value = raw_input('Enter the waiting time to perform I/O : ')
wait_time = int(value)

user_input(number_of_processes)

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
current_procees = get_top_process(ready_queue)

time_line = current_procees[1]
while 1:
    time_line += 1
    if not ready_queue.qsize() is 0:
        make_process_to_complete()

    if  current_procees[11] is IO_Type and current_procees[2] is not 0:
        flag = add_process_to_waiting_queue()
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

        add_to_completed_process_List()

        for i in range(len(process_queue2)):
            if ((time_line >= process_queue2[i][1]) and (last_time < process_queue2[i][1])):
                ready_queue.put(process_queue2[i])
                last_time = time_line


        if len(completed_processes) is number_of_processes:
            break

        if not ready_queue.qsize() is 0:
            current_procees = get_top_process(ready_queue)

    if  current_procees[6] is 0:
        flag = 0
        for i in range(len(process_queue2)):
            add_new_process_to_ready_queue(flag)

        if  flag is not 1:
            current_procees[6] = time_quantum
            ready_queue.put(current_procees)
            pop_current_process(current_procees, ready_queue)

        flag = 0
        last_time = time_line
        current_procees = get_top_process(ready_queue)

calculate_times()
display(number_of_processes, completed_processes, waiting_time_queue, total_waiting_time, turn_around_time)
