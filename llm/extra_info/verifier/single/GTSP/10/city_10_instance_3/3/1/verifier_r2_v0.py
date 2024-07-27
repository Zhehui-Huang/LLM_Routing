import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(tour, total_cost):
    # Cities and their coordinates
    cities = {
        0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
        5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
    }

    # Groups of cities
    groups = [
        [7, 9], [1, 3], [4, 6], [8], [5], [2]
    ]

    # Requirements
    # 1. The robot must start and end the route at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # 2. The robot must visit one and only one city from each of the six city groups
    visited_cities = set(tour[1:-1])  # exclude the first and last depot city
    for group in groups:
        if not any(city in visited_cities for city in group):
            return "FAIL"
        if sum(city in visited_cities for city in group) != 1:
            return "FAIL"
    
    # 3. Travel cost is measured by the Euclidean distance between cities and must match the given total
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Given solution to verify
tour_solution = [0, 7, 1, 4, 8, 5, 2, 0]
total_cost_solution = 324.1817486177585

# Verify the solution
result = verify_solution(tour_solution, total_cost_solution)
print(result)