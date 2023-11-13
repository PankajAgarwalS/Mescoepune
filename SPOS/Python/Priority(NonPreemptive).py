class Process:
    def __init__(self, process_id, burst_time, priority):
        self.process_id = process_id
        self.burst_time = burst_time
        self.priority = priority

def priority_scheduling(processes):
    processes.sort(key=lambda x: x.priority)
    time_chart = []
    total_time = 0

    for process in processes:
        total_time += process.burst_time
        time_chart.append((process.process_id, total_time))

    return time_chart

if __name__ == "__main__":
    # Example processes
    processes = [
        Process(1, 6, 2),
        Process(2, 8, 1),
        Process(3, 4, 3),
        Process(4, 5, 4),
    ]

    time_chart = priority_scheduling(processes)

    # Display the time chart
    print("Time Chart:", time_chart)
