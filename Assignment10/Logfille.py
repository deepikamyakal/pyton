# 2. Log File Analyzer
'''
**Concepts Covered:**
Strings, Lists, Dictionaries, Sets

### Problem Statement
In many real-world systems such as servers, APIs, and cloud platforms, log files are generated to record events. 
These logs contain messages with levels such as **INFO, WARNING, and ERROR**.
Create a Python program that analyzes a collection of log messages and provides useful insights.

### Requirements
The program should:

1. Store log messages in a **list**.
2. Extract the **log level** from each message using string operations.
3. Count how many times each log level appears.
4. Store the counts in a **dictionary**.
5. Identify all unique log levels using a **set**.

### Implementation Guidelines

* Use string methods such as `split()` to separate log components.
* Use a dictionary to track the **frequency of each log level**.
* Use a set to maintain **unique log categories**.

### Expected Outcome
The program should display:
* Total number of each log type
* List of unique log levels found in the logs
'''

logs = [
    "INFO user logged in",
    "ERROR Database connection failed",
    "WARNING Disk space low",
    "INFO File uploaded",
    "ERROR Invalid password",
    "WARNING High memory usage",
    "INFO Logout successful"
]

log_count = {}

unique_levels = set()

for log in logs:
    parts = log.split()
    level = parts[0]
    unique_levels.add(level)

    if level in log_count:
        log_count[level] += 1
    else:
        log_count[level] = 1

print("Log level couts:")
for key, value in log_count.items():
    print(key, ":", value)

print("\nUnique log levels:")
print(unique_levels)   
