import numpy as np

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Tour reported from the solver
tour = [0, 6, 1, 7, 9, 2, 5, 3, 8, 4, 0]
reported_cost = 278.9348447394249

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_travel_cost(tour, cities):
    total_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost += euclidean_distance(cities[city1], cities[city2])
    return total_cost

def verify_tour(tour, cities):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if all cities except depot are visited exactly once
    visited = set(tour[1:-1])
    if len(visited) != len(cities) - 1 or any(city not in visited for city in cities if city != 0):
        return "FAIL"
    
    # Check if the total travel cost is calculated correctly
    calculated_cost = calculate_total_travel_cost(tour, cities)
    if not np.isclose(calculated_cost, reported_cost, atol=1e-3):
        return "FAIL"
    
    return "CORRECT"

# Unit test to verify the solution
test_result = verify_tour(tour, cities)
print(test_result)