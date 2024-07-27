import numpy as np

def calculate_distance(city1, city2):
    return np.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution(robots_tours, cities_coordinates):
    visited_cities = set()
    overall_cost = 0
    
    for robot, tour_info in robots_tours.items():
        tour, cost = tour_info['tour'], tour_info['cost']
        
        # [Requirement 1] Starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL", "[Requirement 1] All tours must start and end at the depot."
        
        # [Requirement 4] Tour output format
        if not all(isinstance(x, int) for x in tour):
            return "FAIL", "Tour format error. All entries should be integers of city indices."
        
        # Calculate tour cost and check [Requirement 3]
        calc_cost = 0
        for i in range(len(tour) - 1):
            calc_cost += calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i + 1]])
        
        # Accounting for floating-point arithmetic issues in comparison
        if not np.isclose(calc_cost, cost, atol=0.1):
            return "FAIL", f"[Requirement 3] Tour cost for {robot} is incorrect. Calculated: {calc_cost}, Provided: {cost}."
        
        visited_cities.update(tour[1:-1])  # exclude depot from visitation check
        
        overall_cost += cost
    
    # [Requirement 2] Every city visited once excluding the depot
    if visited_cities != set(range(1, 16)):
        return "FAIL", "[Requirement 2] Each city must be visited exactly once by any robot, excluding the depot."

    return "CORRECT", f"All checks passed. Overall Cost: {overall_cost}"

# Data
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

robots_tours = {
    0: {'tour': [0, 5, 8, 0], 'cost': 81.03},
    1: {'tour': [0, 12, 15, 0], 'cost': 66.12},
    2: {'tour': [0, 6, 4, 0], 'cost': 57.77},
    3: {'tour': [0, 14, 13, 0], 'cost': 80.99},
    4: {'tour': [0, 3, 9, 0], 'cost': 88.79},
    5: {'tour': [0, 10, 7, 0], 'cost': 61.7},
    6: {'tour': [0, 2, 11, 0], 'cost': 78.25},
    7: {'tour': [0, 1, 0], 'cost': 27.78},
}

# Verification
result, message = verify_solution(robots_tours, cities_coordinates)
print(result)  # Output "CORRECT" or "FAIL"
if result == "FAIL":
    print(message)