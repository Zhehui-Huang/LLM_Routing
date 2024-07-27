import numpy as np

# Provided city coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Given solution tour and cost
tour_solution = [0, 19, 8, 17, 18, 13, 11, 14, 2, 5, 16, 7, 12, 9, 1, 10, 6, 15, 4, 3, 0]
reported_cost = 502.00

def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_total_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost += euclidean_distance(cities[city1], cities[city2])
    return total_cost

def verify_tour(tour, cities, reported_cost):
    # Verify all cities except depot are visited exactly once
    all_cities_visited = set(range(1, 20)) == set(tour[1:-1])
    
    # Verify tour starts and ends at the depot
    starts_ends_depot = tour[0] == 0 and tour[-1] == 0
    
    # Calculate actual total cost and compare with reported cost
    actual_cost = calculate_total_cost(tour, cities)
    cost_matches = np.isclose(actual_cost, reported_cost, atol=1e-2)
    
    # Output results of verification
    if all_cities_visited and starts_ends_depot and cost_matches:
        return "CORRECT"
    else:
        return "FAIL"

# Perform verification and print result
result = verify_tour(tour_solution, cities, reported_cost)
print(result)