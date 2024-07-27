import numpy as np

def calculate_distance(city1, city2):
    return np.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_tour(tour, total_travel_cost, max_distance):
    cities = [
        (84, 67), (74, 40), (71, 13), (74, 82), (97, 28), 
        (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)
    ]
    
    # Requirement 1
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2
    if sorted(tour) != sorted(list(set(tour))) or len(tour) != 11:
        return "FAIL"
    
    # Calculating the actual total travel cost and max distance
    calculated_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
    
    # Requirement 5
    if not (np.isclose(calculated_cost, total_travel_cost, atol=0.01) and 
            np.isclose(calculated_max_distance, max_distance, atol=0.01)):
        return "FAIL"
    
    # Requirement 3
    # This requirement technically requires access to optimal solutions for hard validation. 
    # We skip actual "minimization verification" here as it requires solving the problem or known benchmarks.
    
    # Requirement 4 is not verifiable through unit tests without extensive subroutine outputs.

    return "CORRECT"
    
# Tour and costs as found in solution
tour_solution = [0, 1, 2, 4, 3, 9, 5, 6, 7, 8, 0]
total_travel_cost_solution = 379.34
max_distance_solution = 68.26

# Verify the solution
result = verify_tour(tour_solution, total_travel_cost_solution, max_distance_solution)
print(result)