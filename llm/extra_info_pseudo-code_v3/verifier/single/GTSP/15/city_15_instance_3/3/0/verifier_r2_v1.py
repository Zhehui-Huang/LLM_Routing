import math

# Define the cities and their coordinates
cities = {
    0: (16, 90),  # Depot city
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Define the city groups
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Solution tour and provided cost
solution_tour = [0, 14, 5, 10, 11, 8, 9, 0]
provided_cost = 166.75801920718544

def euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities using their coordinates."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tour(tour, city_groups, provided_cost):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    visited_cities = tour[1:-1]
    for group in city_groups:
        if not any(city in group for city in visited_cities):
            return "FAIL"
    
    calculated_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    if not math.isclose(calculated_cost, provided_cost, rel_tol=1e-6):
        return "FAIL"
    
    return "CORRECT"

# Execute verification
test_result = verify_tour(solution_tour, city_groups, provided_cost)
print(test_result)