import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution(tour, total_cost):
    # City coordinates
    cities = [
        (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
        (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
        (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
        (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
    ]
    
    # Groups of cities
    groups = [
        [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
    ]
    
    # Start and end check
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # One city from each group check
    visited_groups = [0] * len(groups)
    for city in tour[1:-1]:
        for i, group in enumerate(groups):
            if city in group:
                visited_groups[i] += 1
    
    if any(v != 1 for v in visited_groups):
        return "FAIL"

    # Total cost calculation check
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Solution as provided:
tour = [0, 17, 15, 3, 6, 18, 16, 0]
total_cost = 237.06003989507903

# Testing the solution
print(test_solution(tour, total_cost))