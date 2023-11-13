def job_scheduling(jobs):
    # Sort jobs based on their finish times in ascending order
    jobs.sort(key=lambda x: x[1])

    n = len(jobs)
    result = []
    # Initialize array to track time slots
    time_slots = [False] * n

    for i in range(n):
        # Find the latest available time slot for the current job
        for j in range(min(n - 1, jobs[i][0] - 1), -1, -1):
            if not time_slots[j]:
                result.append(jobs[i])
                time_slots[j] = True
                break

    return result

# Example usage:
jobs = [(1, 3), (2, 5), (3, 8), (4, 6)]
scheduled_jobs = job_scheduling(jobs)

print("Scheduled Jobs:")
for job in scheduled_jobs:
    print(f"Job {job[0]} starts at {job[1]}")
