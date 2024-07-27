import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, total_cost):
    # City coordinates
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

    # City groups
    groups = [
        [3, 6],
        [5, 8],
        [4, 9],
        [1, 7],
        [2]
    ]

    # [Requirement 1] Check start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Check exactly one city from each group is visited
    group_visits = {i: False for i in range(len(groups))}
    for city in tour[1:-1]:  # exclude the depot city in the beginning and end
        for idx, group in enumerate(groups):
            if city in group:
                if group_visits[idx]:
                    return "FAIL"
                group_visits[idx] = True
    
    if not all(group_visits.values()):
        return "FAIL"

    # [Requirement 3] Check if the total travel cost is correctly calculated
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Given solution
tour = [0, 3, 5, 9, 1, 2, 0]
total_cost = 281.60273931778477
result = check_solution(tour, total_cost)
print(result)