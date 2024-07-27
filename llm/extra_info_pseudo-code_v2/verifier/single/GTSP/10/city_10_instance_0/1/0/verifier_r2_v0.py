import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, total_cost):
    cities = {
        0: (50, 42),
        1: (41, 1),
        2: (18, 46),
        3: (40, 98),
        4: (51, 69),
        5: (47, 39),
        6: (62, 26),
        7: (79, 31),
        8: (61, 90),
        9: (42, 49)
    }
    
    groups = {
        0: [1, 2, 6],
        1: [3, 7, 8],
        2: [4, 5, 9]
    }

    # Check if all cities are present and have distinct coordinates
    if len(set(cities.values())) != 10:
        return "FAIL"
    
    # Check if starting and ending city is 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_from_groups = set()
    for idx in tour[1:-1]:  # Skip the depot at beginning and end
        for g_index, group in groups.items():
            if idx in group:
                if g_index in visited_from_groups:
                    return "FAIL"
                visited_from_groups.add(g                                                   _index)
    if len(visited_from_groups) != len(groups):
        return "FAIL"

    # Check the total travel cost
    calculated_cost = 0.0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Solution provided
tour_provided = [0, 6, 7, 5, 0]
total_cost_provided = 74.94753083872993

# Verify the solution
result = verify_solution(tour_provided, total_cost_provided)
print(result)