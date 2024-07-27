import math

# Given cities and their coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20),
    4: (18, 61), 5: (40, 57), 6: (57, 30), 7: (36, 12),
    8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
    12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Given groups
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Provided tour and its calculated cost
provided_tour = [0, 5, 10, 4, 11, 0]
provided_cost = 184.24203302868492

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, groups, expected_cost):
    if not tour:
        return "FAIL"
    
    # Check if the tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if tour visits exactly one city from each group
    visited_groups = [set(group) & set(tour[1:-1]) for group in groups]
    if any(len(group) != 1 for group in visited_groups):
        return "FAIL"
    
    # Calculate the travel cost of the tour
    total_cost = 0.0
    for i in range(len(tour) - 1):
        city1, city2 = tour[i], tour[i + 1]
        total_cost += calculate_euclidean_distance(cities[city1], cities[city2])
    
    # Compare the calculated cost with the provided cost
    if not math.isclose(total_cost, expected_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Unit Test Execution
result = verify_tour(provided_tour, groups, provided_cost)
print(result)