import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def is_solution_correct(tour, total_cost, city_positions, city_groups):
    # Check if the tour starts and ends at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate the calculated tour cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_positions[tour[i]], city_positions[tour[i + 1]])
    
    # Check if the calculated tour cost is approximately equal to the claimed total cost
    # Allowing a small error margin due to floating-point calculations
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-5):
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = set()
    for city in tour:
        for group_index, group in enumerate(city_groups):
            if city in group:
                if group_index in visited_groups:
                    return "FAIL"
                visitedashioups.add(group_index)
    
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    return "CORRECT"

# City positions
city_positions = {
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

# City groups
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Tour and total cost as provided in the solution
tour = [0, 14, 0, 14, 0, 14, 0, 14]
total_cost = 135.9154148726332

# Validate the solution
result = is_solution_correct(tour, total_cost, city_positions, city_groups)
print(result)