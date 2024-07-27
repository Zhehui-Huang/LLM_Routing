import math

# Coordinates of the cities
cities = {
    0: (29, 51),  # Depot
    1: (49, 20),
    2: (79, 69),
    5: (40, 57),
    6: (57, 30),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    13: (60, 50),
    3: (17, 20),
    4: (18, 61),
    7: (36, 12),
    11: (78, 82),
    12: (83, 96),
    14: (98, 1),
}

# Solution obtained from solver
tour = [0]
total_travel_cost = 0

# Requirement 1: Check if the tour starts and ends at depot city (city 0)
def check_start_end(tour):
    return tour[0] == 0 and tour[-1] == 0

# Requirement 2: Check if the robot visits exactly one city from each group
city_groups = [
    [1, 2, 5, 6],  # Group 0
    [8, 9, 10, 13],  # Group 1
    [3, 4, 7],  # Group 2
    [11, 12, 14]  # Group 3
]

def check_one_city_per_group(tour):
    visited_groups = [False] * len(city_groups)
    for city in tour:
        for idx, group in enumerate(city_groups):
            if city in group:
                if visited_groups[idx]:
                    return False
                visited_occurences[idx] = True
    return all(visited_groups)

# Requirement 3: Check if the cost is minimized (validating cost is more complex without all possible tours for comparison)
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_cost(tour, reported_cost):
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(tour[i], tour[i + 1])
    return math.isclose(calculated_cost, reported_cost, rel_tol=1e-9)

# Unit tests execution
if (check_start_end(tour) and 
    check_one_city_per_group(tour) and 
    check_cost(tour, total_travel_cost)):
    print("CORRECT")
else:
    print("FAIL")