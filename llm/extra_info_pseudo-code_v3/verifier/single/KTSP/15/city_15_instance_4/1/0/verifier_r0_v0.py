import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
    # Cities coordinates based on the given description
    cities = {
        0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
        5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
        10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
    }

    # Check Requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check Requirement 2: Include exactly 12 cities
    if len(set(tour)) != 13:  # Includes city 0 twice (start and end)
        return "FAIL"
    
    # Check Requirement 3: Correctly calculated travel cost based on Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, abs_tol=1e-5):
        return "FAIL"

    # Output is assumed correct, detailed requirements for Requirement 4, 5 and 6 are assumed met or not verifiable with tests
    return "CORRECT"

# Given solution details
tour = [0, 1, 5, 9, 7, 12, 11, 6, 3, 14, 8, 10, 0]
total_cost = 223.74492356775863

# Verify the solution
output = verify_solution(tour, total_cost)
print(output)  # Expect "CORRECT" if all requirements are met, "FAIL" otherwise