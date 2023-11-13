def fcfs(processes, burst_time):
    n = len(processes)

    # Waiting time for the first process is 0
    waiting_time = [0]

    # Calculate waiting time for each process
    for i in range(1, n):
        waiting_time.append(waiting_time[i - 1] + burst_time[i - 1])

    # Calculate turnaround time for each process
    turnaround_time = [waiting_time[i] + burst_time[i] for i in range(n)]

    # Calculate average waiting time and turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    # Display results
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{i + 1}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")


# Example usage
if __name__ == "__main__":
    # Example processes and burst times
    processes = [1, 2, 3, 4, 5]
    burst_time = [10, 5, 8, 7, 3]

    # Run FCFS scheduling
    fcfs(processes, burst_time)
