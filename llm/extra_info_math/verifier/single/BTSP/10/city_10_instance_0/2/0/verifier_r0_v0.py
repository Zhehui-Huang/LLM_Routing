import numpy as np

# City coordinates given in the environment information
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46), 3: (40, 98), 4: (51, 69),
    5: (47, 39), 6: (62, 26), 7: (79, 31), 8: (61, 90), 9: (42, 49)
}

# Result from the MILP solver
tour = [0, 1, 6, 7, 5, 2, 9, 8, 3, 4, 0]
total_travel_cost = 305.0457065108971
max_distance_between_cities = 45.18849411078001

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities"""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, total_travel_cost, max_distance_between_cities):
    # Check Requirement 1: Journey starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: All cities visited exactly once
    all_cities = set(range(len(cities)))
    visited_cities = set(tour[1:-1]) # Excluding the starting and ending depot
    if visited_cities != all_cities - {0}:
        return "FAIL"
    
    # Calculate the total cost and max distance using Euclidean distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(tour[i], tour[i+1])
        calculated_total_cost += dist
        if dist > calculated_max_distance:
            calculated_max_distance = dist
    
    # Check Requirement 3: Max distance is minimized
    if not np.isclose(calculated_max_distance, max_distance_between_cities, atol=1e-6):
        return "FAIL"
    
    # Check the total travel cost for consistency
    if not np.isclose(calculated_total_cost, total_travel_cost, atol=1e-6):
        return "FAIL"

    return "CORRECT"

# Run the verification code
test_result = verify_tour(tour, total_travel_cost, max_distance_between_cities)
print(test_result)