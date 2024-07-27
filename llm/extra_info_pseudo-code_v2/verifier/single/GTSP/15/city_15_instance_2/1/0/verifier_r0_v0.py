import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour_and_cost(tour, total_cost):
    # Coordinates of the cities
    coordinates = [(54, 87), (21, 84), (69, 84), (53, 40), (54, 42), 
                   (36, 30), (52, 82), (93, 44), (21, 78), (68, 14), 
                   (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)]
    group_indices = [[8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]]
    
    # Requirement 1: Start and End at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each group
    visited_groups = set()
    for city in tour[1:-1]:
        found_group = False
        for i, group in enumerate(group_indices):
            if city in group:
                if i in visited_groups:
                    return "FAIL"
                visited_groups.add(i)
                found_group = True
                break
        if not found_group:
            return "FAIL"
    if len(visited_groups) != len(group_indices):
        return "FAIL"

    # Requirement 3: Cost calculation check
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += calculate_euclidean_distance(coordinates[city1][0], coordinates[city1][1], 
                                                        coordinates[city2][0], coordinates[city2][1])
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"

    # All checks passed
    return "CORRECT"

# Given solution data
tour_solution = [0, 12, 10, 4, 3, 2, 0]
tour_cost = 138.15244358342136

# Verify the solution
result = verify_tour_and_cost(tour_solution, tour_cost)
print(result)