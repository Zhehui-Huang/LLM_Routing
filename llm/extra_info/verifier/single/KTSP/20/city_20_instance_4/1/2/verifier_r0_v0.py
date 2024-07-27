import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cost):
    # Define the cities coordinates
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
        (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), 
        (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]

    # [Requirement 1] Start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Visit exactly 16 different cities, including the depot
    if len(tour) != 16 + 1 or len(set(tour)) != 16:
        return "FAIL"

    # [Requirement 4] Calculate the travel cost using Euclidean distance and compare with given cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(calculated_cost, cost, rel_tol=1e-2):  # using relative tolerance for floating point comparisons
        return "FAIL"

    # Passed all checks
    return "CORRECT"

# Provided Tour and Total travel cost
tour = [0, 8, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 6, 10, 0]
cost = 285.96

# Verify the solution
result = verify_solution(tour, cost)
print(result)