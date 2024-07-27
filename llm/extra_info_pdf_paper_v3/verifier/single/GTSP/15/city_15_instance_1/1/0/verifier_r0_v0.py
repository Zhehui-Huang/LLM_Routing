import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_solution():
    # Cities coordinates
    coordinates = [
        (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
        (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
        (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
    ]
    
    # Groups of cities
    groups = [
        [1, 2, 5, 6],
        [8, 9, 10, 13],
        [3, 4, 7],
        [11, 12, 14]
    ]
    
    # Provided solution
    tour = [0, 5, 10, 4, 11, 0]
    reported_cost = 184.24203302868492
    
    # [Requirement 1] Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Visit exactly one city from each group
    visited_groups = [0] * len(groups)
    for city in tour[1:-1]:
        for i, group in enumerate(groups):
            if city in group:
                visited_groups[i] += 1
    if visited_groups != [1, 1, 1, 1]:
        return "FAIL"
    
    # [Requirement 3] Each city must be visited exactly once, except depot
    unique_cities = set(tour)
    if len(unique_cities) != len(tour) - 1:
        return "FAIL"
    
    # [Requirement 4] Calculate travel cost using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-9):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Running the test
print(test_solution())