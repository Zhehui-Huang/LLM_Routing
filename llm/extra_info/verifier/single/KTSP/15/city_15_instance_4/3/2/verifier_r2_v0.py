import math

def calculate_distance(c1, c2):
    return math.sqrt((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2)

def verify_solution(tour, claimed_cost, cities):
    # Check Requirement 1 and 4: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Visit exactly 12 cities including the depot
    if len(set(tour)) != 12:
        return "FAIL"

    # Check Requirement 6, 5 and 7: Calculated travel cost should match the given cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(calculated_cost, claimed_cost, rel_tol=1e-2):
        return "FAIL"

    # If all checks pass:
    return "CORRECT"

# Define the cities based on the task description
cities = {
    0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90), 
    5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44), 
    10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
}

# Proposed solution to check
tour_solution = [0, 1, 10, 5, 8, 14, 13, 3, 11, 9, 6, 12, 0]
total_travel_cost = 331.79

# Check the solution
result = verify_solution(tour_solution, total_travel, cities)
print(result)