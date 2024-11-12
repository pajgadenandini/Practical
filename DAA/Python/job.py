import pandas as pd
from tabulate import tabulate

class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs):
    # Sort jobs in descending order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Find the maximum deadline to know the number of time slots
    max_deadline = max(job.deadline for job in jobs)

    # Initialize time slots, all initially unoccupied
    time_slots = [-1] * max_deadline  # -1 means slot is empty
    total_profit = 0

    # Iterate through each job in descending profit order
    for job in jobs:
        # Try to schedule the job in its last possible slot before its deadline
        for j in range(job.deadline - 1, -1, -1):
            if time_slots[j] == -1:  # If the slot is empty
                time_slots[j] = job.job_id  # Assign job to this slot
                total_profit += job.profit  # Add job's profit to total profit
                break

    # Collect and return the job sequence and total profit
    scheduled_jobs = [job_id for job_id in time_slots if job_id != -1]
    return jobs, scheduled_jobs, total_profit, time_slots

# Dynamic input
n = int(input("Enter the number of jobs: "))
jobs = []
for i in range(n):
    job_id = input(f"Enter job ID for job {i + 1}: ")
    deadline = int(input(f"Enter deadline for job {i + 1}: "))
    profit = int(input(f"Enter profit for job {i + 1}: "))
    jobs.append(Job(job_id, deadline, profit))

# Get the result of job sequencing
jobs_input, scheduled_jobs, total_profit, time_slots = job_sequencing(jobs)

# Display Input Jobs as Table (like Gantt chart)
input_data = {
    'Job ID': [job.job_id for job in jobs_input],
    'Deadline': [job.deadline for job in jobs_input],
    'Profit': [job.profit for job in jobs_input]
}
input_df = pd.DataFrame(input_data)

# Display the Time Slot Gantt chart
gantt_chart_data = {'Time Slot': [f"Slot {i+1}" for i in range(len(time_slots))], 'Job Scheduled': time_slots}
gantt_df = pd.DataFrame(gantt_chart_data)

# Display the Scheduled Jobs
scheduled_jobs_data = {'Scheduled Jobs': scheduled_jobs}

# Print the DataFrames with borders using `tabulate`
print("\nInput Jobs (Job ID, Deadline, Profit):")
print(tabulate(input_df, headers='keys', tablefmt='grid', showindex=False))

print("\nGantt Chart (Job Scheduling):")
print(tabulate(gantt_df, headers='keys', tablefmt='grid', showindex=False))

print(f"\nScheduled Jobs: {scheduled_jobs}")
print(f"Total Profit: {total_profit}")

















































# Enter the number of jobs: 3
# Enter job ID for job 1: A
# Enter deadline for job 1: 2
# Enter profit for job 1: 100
# Enter job ID for job 2: B
# Enter deadline for job 2: 1
# Enter profit for job 2: 50
# Enter job ID for job 3: C
# Enter deadline for job 3: 2
# Enter profit for job 3: 200

# Input Jobs (Job ID, Deadline, Profit):
#   Job ID  Deadline  Profit
# 0      C         2     200
# 1      A         2     100
# 2      B         1      50

# Gantt Chart (Job Scheduling):
#   Time Slot Job Scheduled
# 0    Slot 1             A
# 1    Slot 2             C

# Scheduled Jobs: ['A', 'C']
# Total Profit: 300

# Enter the number of jobs: 4
# Enter job ID for job 1: j1
# Enter deadline for job 1: 2
# Enter profit for job 1: 50
# Enter job ID for job 2: j2
# Enter deadline for job 2: 1
# Enter profit for job 2: 15
# Enter job ID for job 3: j3
# Enter deadline for job 3: 2
# Enter profit for job 3: 10
# Enter job ID for job 4: j4
# Enter deadline for job 4: 1
# Enter profit for job 4: 25

# Input Jobs (Job ID, Deadline, Profit):
#   Job ID  Deadline  Profit
# 0     j1         2      50
# 1     j4         1      25
# 2     j2         1      15
# 3     j3         2      10

# Gantt Chart (Job Scheduling):
#   Time Slot Job Scheduled
# 0    Slot 1            j4
# 1    Slot 2            j1

# Scheduled Jobs: ['j4', 'j1']
# Total Profit: 75

# Summary of Complexities:
# Scenario	Time Complexity	Space Complexity
# Best Case	
# 𝑂(𝑛^2)
# O(n)
# Worst Case	
# 𝑂(𝑛2)
# O(n)
# Average Case	
# 𝑂(𝑛^2)
# O(n)
# Discussion on Complexities:
# Time Complexity:

# Worst-case time complexity is 
# 𝑂(𝑛^2) because, in the worst case, for each job, we may have to check all available slots (up to 
# 𝑛
# n slots).
# However, best-case and average-case time complexities are also 
# 𝑂(𝑛^2)because of the sorting step and the slot-checking step for each job.
# Even though we might find slots more efficiently in some cases, we can't escape the fact that, in general, we need to check multiple time slots for each job, which results in 
# 𝑂(𝑛^2) behavior.
# Space Complexity:

# Space complexity is
# O(n) as we store:
# The list of jobs,
# The list of time slots (which is at most 
# n long),
# The result (the scheduled jobs and total profit).
# This is relatively efficient because we only store the necessary data for scheduling and results. We don’t need extra data structures beyond the job list and time slots.
