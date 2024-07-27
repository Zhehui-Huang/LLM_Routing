import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost, city_positions, city_groups):
    # [Requirement 1]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2]
    visited_groups = set()
    for city in tour[1:-1]:
        for group_index, group in enumerate(citygroups):
            if city in group:
                visited_groups.add(group_index)
                break
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # [Requirement 3] and [Reqirement 4]
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(city_positions[tour[i]], city_positions[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Define city positions and groups
city_positions = [
    (84, 67),  # Depot city 0
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

city_groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Provided solution
tour = [0, 7, 1, 4, 8, 5, 2, 0]
total_cost = 324.1817486177585

# Verify the solution
result = verify_solution(tour, total_cost, city_positions, city_groups)
print(result)