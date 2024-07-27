import math

# City coordinates according to the problem statement
cities = {
    0: (16, 90),
    1: (43, 99),  # Group 0
    6: (6, 61),   # Group 0
    14: (32, 79), # Group 0
    5: (34, 73),  # Group 1
    12: (70, 95), # Group 1
    13: (29, 64), # Group 1
    7: (86, 69),  # Group 2
    10: (42, 64), # Group 2
    4: (54, 93),  # Group 3
    11: (64, 30), # Group 3
    2: (80, 21),  # Group 4
    8: (30, 50),  # Group 4
    3: (86, 92),  # Group 5
    9: (35, 73)   # Group 5
}

# Groups of cities
city_groups = {
    0: [1, 6, 14],
    1: [5, 12, 13],
    2: [7, 10],
    3: [4, 11],
    4: [2, 8],
    5: [3, 9]
}

# Result from the optimization model
tour = [0, 0]
total_travel_cost = 0.0

# Unit test to check if the solution is correct

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Check [Requirement 1]
def check_start_end(tour):
    return tour[0] == 0 and tour[-1] == 0

# Check [Requirement 2]
def check_one_per_group(tour):
    visited = set(tour)
    for group in city_groups.values():
        if len(visited.intersection(set(group))) != 1:
            return False
    return True

# Check [Requirement 3]
def check_total_cost(tour, reported_cost):
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += euclidean_distance(tour[i-1], tour[i])
    return abs(calculated_result - reported_cost) < 1e-5

# Test the results
if (check_start_end(tour) and 
    check_one_per_group(tour) and 
    check_total_cost(tour, total_travel_cost)):
    print("CORRECT")
else:
    print("FAIL")