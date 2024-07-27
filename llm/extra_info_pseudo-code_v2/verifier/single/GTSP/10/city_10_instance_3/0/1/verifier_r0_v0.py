import math

# Input data
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}
city_groups = {
    0: [7, 9],
    1: [1, 3],
    2: [4, 6],
    3: [8],
    4: [5],
    5: [2]
}

# Solution provided
tour = [0, 7, 1, 4, 8, 5, 2, 0]
reported_total_cost = 324.1817486177585

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, reported_cost):
    # Check if the tour starts and ends at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if each group is represented exactly once
    groups_represented = [0] * len(city_groups)
    for city in tour[1:-1]:  # skip the first and last as they are the depot city
        for group_id, members in city_groups.items():
            if city in members:
                if groups_represented[group_id] != 0:
                    return "FAIL"
                groups_represented[group_id] = 1
    if sum(groups_represented) != len(city_groups):
        return "FAIL"
    
    # Calculate total cost and compare it with reported cost
    total_cost_calculated = 0
    for i in range(len(tour) - 1):
        total_cost_calculated += calculate_distance(tour[i], tour[i + 1])
    
    if not math.isclose(total_cost_calculated, reported_cost, abs_tol=1e-4):
        return "FAIL"
    
    return "CORRECT"

# Function call to check the solution against the requirements
print(verify_solution(tour, reported_total_cost))