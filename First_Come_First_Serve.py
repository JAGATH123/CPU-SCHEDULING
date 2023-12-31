# FCFS Algorithm with and without Arrival Time

# To Find - Turn Around Time and Wait Time and their respective average times

from tabulate import tabulate # For printing the result in a Tabular Format


def sorting_arrival(l):
    return l[1] # Returns the Second element of the list which is Arrival Time


def Turn_Around_Time(P, limit):
    # Declaring Variables for Calculating Total Turn Around Time
    total_tat = 0
    for i in range(limit):
        tat = P[i][3] - P[i][1]
        total_tat += tat # Formula For Turn Around Time -> Completion Time - Arrrival TIme
        P[i].append(tat) # Appending the Turn Around Time to the List

    avg_tat = total_tat/limit
    return avg_tat



def Waiting_Time(P, limit):
    # Declaring Variables for Calculating Total Waiting Time
    total_wt = 0

    for i in range(limit):
        wt = P[i][4] - P[i][2]
        total_wt += wt # Formula For Waiting Time -> Turn Around Time - Burst TIme
        P[i].append(wt) # Appending the Waiting Time to the List

    avg_wt = total_wt/limit
    return avg_wt
        

def Logic(P, limit):
    completion_time = 0
    exit_time = []
    
    for i in range(limit):
        if completion_time < P[i][1]:
            completion_time = P[i][1]
        completion_time += P[i][2]
        exit_time.append(completion_time)
        P[i].append(completion_time)
    
    tat = Turn_Around_Time(P, limit)
    wt = Waiting_Time(P, limit)

    P.sort(key=sorting_arrival) # Sorting the List by Arrivak Time
    headers = ["Process Number", "Arrival Time", "Burst Time", "Completion Time", "Turn Around Time", "Waiting Time"]
    print(tabulate(P, headers, tablefmt="psql"))

    # Printing the Average Waiting and Turn Around Time
    print("\nAverage Waiting Time is = ", round(wt, 2)) # Rounding off Average Waiting Time to 2 Decimal places
    print("Average Turn Around Time is = ", round(tat, 2)) # Rounding off Average Turn Around Time to 2 Decimal places


# Main Function
def main():
    run = True
    while(run):

        # Declaring arrays
        processes = []

        print("\nMenu\nDo you want to assume : \n1. Arrival Time as 0\n2. Input Arrival Time\n3. Exit\n")
        ch = int(input("Enter Your Choice : "))

        if ch == 1:
            limit_process = int(input("Enter the Number of Processes : "))
            for i in range(limit_process):
                p = []
                arrival = 0
                burst = int(input("Enter the Burst Time for process {} : ".format(i)))
                process_id = "P" + str(i + 1)

                p.extend([process_id, arrival, burst])
                processes.append(p)

            Logic(processes, limit_process)
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))

        elif ch == 2:
            limit_process = int(input("Enter the Number of Processes : "))
            for i in range(limit_process):
                p = []
                arrival = int(input("Enter the Arrival Time for process {} : ".format(i)))
                burst = int(input("Enter the Burst Time for process {} : ".format(i)))
                process_id = "P" + str(i + 1)

                p.extend([process_id, arrival, burst])
                processes.append(p)
                

            Logic(processes, limit_process)
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))
        
        elif ch == 3:
            print("Thank You!")
            exit(0)

        else:
            print("Invalid Choice!")
            run = int(input("\nWant to continue? (Yes = Input 1/false = Input 0) : "))


# Calling the Main Function
main()
