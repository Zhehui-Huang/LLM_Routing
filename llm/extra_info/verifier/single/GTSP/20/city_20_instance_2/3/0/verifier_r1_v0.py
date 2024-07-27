import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost_claimed):
    cities = [
        (3, 26),   # City 0: Depot
        (85, 72),  # City 1
        (67, 0),   # City 2
        (50, 99),  # City 3
        (61, 89),  # City 4
        (91, 56),  # City 5
        (2, 65),   # City 6
        (38, 68),  # City 7
        (3, 92),   # City 8
        (59, 8),   # City 9
        (30, 88),  # City 10
        (30, 53),  # City 11
        (11, 14),  # City 12
        (52, 49),  # City 13
        (18, 49),  # City 14
        (64, 41),  # City 15
        (28, 49),  # City 16
        (91, 94),  # City 17
        (51, 58),  # City 18
        (30, 48)   # City 19
    ]
    groups = [
        [7, 10, 11, 12],
        [3, 8, 13, 16],
        [2, 4, 15, 18],
        [1, 9, 14, 19],
        [5, 6, 17]
    ]

    # Check if tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each group is exactly visited once
    visited_groups = set()
    for city in tour[1:-1]:
        for idx, group in enumerate(groups):
            if city in group:
                visited-elements.add(idx)
    if len(visited_elements) != len(groups):
        return "FAIL"

    # Calculate the claimed total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    # Check if costs match
    if not math.isclose(calculated_cost, total_cost_claimed, abs_tol=0.1):
        return "FAIL"

    return "CORRECT"

# Provided solution
tour = [0, 11, 16, 18, 19, 6, 0]
total_cost_claimed = 162.38

print(verify_solution(tour, total_cost_claimed))