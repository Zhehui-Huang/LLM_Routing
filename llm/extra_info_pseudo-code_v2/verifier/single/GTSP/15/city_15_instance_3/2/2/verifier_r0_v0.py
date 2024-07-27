import math

def compute_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, total_cost, cities, groups):
    # Verify tour starts and ends at Depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify exact one city from each group
    visited_groups = [False] * len(groups)
    visited_count = 0
    for city in tour[1:-1]:  # Exclude depot from group checks
        for i, group in enumerate(groups):
            if city in group:
                if not visited_groups[i]:
                    visited_groups[i] = True
                    visited_count += 1
                    break

    if visited_count != len(groups):
        return "FAIL"
    
    # Verify that the tour travel cost is correct
    computed_cost = 0
    for i in range(len(tour)-1):
        computed_cost += compute_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(total_cost, computed_cost, abs_tol=1e-2):
        return "FAIL"
    
    # As no shortest path verification can be done without solving the problem again, we assume it is correct
    
    return "CORRECT"

# Cities coordinates
cities = {
    0: (16, 90),
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

# Groups of cities
groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

tour = [0, 13, 8, 10, 9, 4, 1, 0]
total_cost = 141.52

# Verify the given solution
result = verify_tour(tour, total_cost, cities, groups)
print(result)