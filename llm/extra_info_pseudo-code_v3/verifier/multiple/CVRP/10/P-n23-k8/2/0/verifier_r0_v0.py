import numpy as np

# Hypothetical solution example based on the 'number of robots', 'demands', and 'capacity'
# It assumes this is the solution from the algorithm not provided in the Python format before.
# Each element in the list represents the tour for each robot as list of cities visited.

solution = [
    [0, 1, 2, 3, 0],       # Robot 0 tour
    [0, 4, 5, 0],           # Robot 1 tour
    [0, 6, 7, 8, 0],        # Robot 2 tour
    [0, 9, 10, 11, 0],      # Robot 3 tour
    [0, 12, 13, 14, 0],     # Robot 4 tour
    [0, 15, 16, 17, 0],     # Robot 5 tour
    [0, 18, 19, 20, 0],     # Robot 6 tour
    [0, 21, 22, 0]          # Robot 7 tour
]

# Demands of each city, index corresponds to city number
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Maximum capacity of each robot
capacity = 40

def check_completeness(demands, solution):
    visited = [False] * len(demands)
    for tour in solution:
        for city in tour:
            visited[city] = True
    # All cities must be visited (except depot multiple times)
    return all(visited[1:])  # skip depot city at index 0

def check_capacity(demands, solution, capacity):
    for tour in solution:
        load = sum(demands[city] for city in tour)
        # Subtracting demand of depot since it is added twice once while coming and second while going
        load -= demands[tour[0]] + demands[tour[-1]]
        if load > capacity:
            return False
    return True

def check_start_end_depot(solution):
    for tour in solution:
        if tour[0] != 0 or tour[-1] != 0:
            return False
    return True

def verify_solution():
    if (check_start_end_depot(solution) and 
        check_capacity(demands, solution, capacity) and 
        check_completeness(demands, solution)):
        return "CORRECT"
    else:
        return "FAIL"

# Output the verification result
print(verify_solution())