import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, costs, all_cities, groups):
    # Check start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Track visited cities to ensure one city per group is visited
    visited_groups = set()
    for city in tour[1:-1]:  # omitting the start and end city in checks, as they are the depot
        for idx, group in enumerate(groups):
            if city in group:
                if idx in visited_groups:
                    return "FAIL"
                visited_groups.add(idx)
    
    # All groups need to be visited exactly once
    if len(visited_groups) != len(groups):
        return "FAIL"
    
    # Verify the tour is continuous and calculate total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(all_cities[tour[i]], all_cities[tour[i+1]])
    if not math.isclose(calculated_cost, costs, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Defining city coordinates and groups
city_coordinates = [
    (16, 90),  # Depot city
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Cost as provided by the solver
total_travel_cost = 172.47424547552504

# Tour provided
tour = [0, 14, 5, 10, 4, 8, 9, 0]

# Calling the verification function
print(verify_solution(tour, total_travel_cost, city_coordinates, city_groups))