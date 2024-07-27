import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_solution(tour, cost):
    cities = [
        (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
        (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
        (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
    ]
    groups = [
        [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9],
        [2, 4, 14], [10, 17], [7, 15]
    ]
    
    # Check if starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Checking unique cities coverage
    visited_cities = set(tour)
    if len(visited_cities) != len(tour):
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = [0] * len(groups)
    for city in tour:
        for i, group in enumerate(groups):
            if city in group:
                visited_groups[i] += 1
    if any(count != 1 for count in visited_groups if count == 0):
        return "FAIL"
    
    # Validate cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])

    # Allow for small floating-point tolerance on costs
    if not math.isclose(calculated_cost, cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided solution data
tour = [0, 8, 17, 9, 12, 6, 4, 15, 0]
cost = 187.15997262302858

# Check the solution
print(validate_solution(tour, cost))