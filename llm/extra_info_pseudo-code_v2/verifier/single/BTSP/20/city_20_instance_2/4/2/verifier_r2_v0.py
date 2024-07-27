import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, total_travel_cost, max_distance):
    cities = {
        0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
        5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
        10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
        15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
    }

    # [Requirement 2] Check if tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 1] Check if each city is visited exactly once
    unique_cities = set(tour[1:-1])  # Excluding the start/end depot city
    if len(unique_cities) != 19:  # Should be 19 unique cities, excluding the depot city
        return "FAIL"

    # [Requirement 6] Check if tour format is correct
    if len(tour) != 21:  # Should include 20 cities plus returns to depot
        return "FAIL"
    
    # [Requirement 3] Check the travel cost
    calculated_cost = 0
    calculated_max = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_cost += dist
        if dist > calculated_max:
            calculated_max = dist

    # Compare the calculated cost with the given total and max distance
    if not (math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-2) and 
            math.isclose(calculated_max, max_distance, rel_tol=1e-2)):
        return "FAIL"

    # [Requirement 4] Already used max_distance check from provided data

    # [Requirement 5] This requirement is about the method used, which we can't verify just by final data
    # Assumption here we trust that it was followed
    
    return "CORRECT"

# Given tour and metrics
tour = [0, 12, 14, 16, 19, 11, 7, 18, 13, 15, 9, 2, 10, 3, 4, 1, 5, 17, 6, 8, 0]
total_cost = 573.20
max_dist = 95.46

# Running the check
result = check_solution(tour, total_cost, max_dist)
print(result)