import math

# Define the city coordinates
cities = {
    0: (3, 26), 
    1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89), 5: (91, 56), 6: (2, 65), 7: (38, 68), 
    8: (3, 92), 9: (59, 8), 10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49), 
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Define the city groups
city_groups = {
    0: [7, 10, 11, 12],
    1: [3, 8, 13, 16],
    2: [2, 4, 15, 18],
    3: [1, 9, 14, 19],
    4: [5, 6, 17],
}

# Given solution Tour and cost
solution_tour = [0]
solution_cost = 0

# Function to calculate Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Validate the solution
def verify_solution(tour, cost):
    # Requirement 1: Tour should start and end at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Tour must visit exactly one city from each group
    visited_cities = set(tour)
    for group in city_groups.values():
        if not visited_cities.intersection(group):
            return "FAIL"
    
    # Requirement 3: Verify the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(tour[i], tour[i+1])
    if not math.isclose(calculated_cost, cost, abs_tol=1e-6):
        return "FAIL"
    
    return "CORRECT"

# Execute the verification
result = verify_solution(solution_tour, solution_cost)
print(result)