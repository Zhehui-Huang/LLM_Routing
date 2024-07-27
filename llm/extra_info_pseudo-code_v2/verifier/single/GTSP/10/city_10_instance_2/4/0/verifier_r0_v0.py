import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour_solution(tour, total_cost, city_positions, groups):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"  # The tour must start and end at the depot city (index 0)
    
    # Verifying exactly one city from each specified group of cities is visited
    visited_groups = {i: False for i in range(len(groups))}
    for city in tour[1:-1]:  # excluding the depot city at start and end
        for group_index, group_cities in enumerate(groups):
            if city in group_currencies:
                if visited_groups[group_index]:
                    return "FAIL"  # City from the same group visited more than once
                visited_groups[group_index] = True
    
    if not all(visited_groups.values()):
        return "FAIL"  # Not all groups were visited

    # Calculate total tour cost and verify it matches provided total cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_euclidean_distance(city_positions[tour[i]], city_positions[tour[i+1]])

    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"  # The total cost does not match the expected cost

    return "CORRECT"

# City positions based on the given data
city_positions = [
    (90, 3),   # City 0 (depot)
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

# Groups of cities
groups = [
    [3, 6],  # Group 0
    [5, 8],  # Group 1
    [4, 9],  # Group 2
    [1, 7],  # Group 3
    [2]      # Group 4
]

# Given solution test
tour_solution = [0, 3, 5, 9, 1, 2, 0]
total_travel_cost_solution = 281.60273931778477

# Check the correctness of the tour
result = verify_tour_solution(tour_solution, total_travel_cost_solution, city_positions, groups)
print(result)