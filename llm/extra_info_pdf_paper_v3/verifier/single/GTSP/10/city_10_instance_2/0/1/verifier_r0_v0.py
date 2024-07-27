import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, cities, groups):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL, tour must start and end at city 0"
    
    # Ensure all groups are represented exactly once
    group_representation = set()
    for city in tour[1:-1]:  # Exclude the starting and ending depot city
        for group_index, group in enumerate(groups):
            if city in group:
                if group_index in group_representation:
                    return "FAIL, duplicate city from a single group"
                else:
                    group_representation.add(group_index)
    if len(group_representation) != len(groups):
        return "FAIL, not all groups are represented"

    # Verify the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return f"FAIL, incorrect total travel cost: expected {calculated_cost}, got {total_cost}"

    return "CORRECT"

# Input data
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

groups = [
    [3, 6],  # Group 0
    [5, 8],  # Group 1
    [4, 9],  # Group 2
    [1, 7],  # Group 3
    [2]      # Group 4
]

# Provided solution
tour_solution = [0, 3, 5, 2, 1, 9, 0]
total_cost_solution = 273.31

# Test
print(verify_solution(tour_solution, total_cost_solution, cities, groups))