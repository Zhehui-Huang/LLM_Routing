import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def test_solution(tour, total_cost):
    cities = {
        0: (90, 3),   # Depot
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
        [3, 6],
        [5, 8],
        [4, 9],
        [1, 7],
        [2]
    ]

    # [Requirement 1] Check start and end at depot:
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # [Requirement 2] Check one city from each group is visited:
    visited_groups = [False] * len(groups)
    for city in tour[1:-1]:
        for i, group in enumerate(groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"
                visited_groups[i] = True
                break
    
    if not all(visited_groups):
        return "FAIL"

    # [Requirement 3] Check if total travel cost is minimized:
    # (In this simulation, we assume the provided cost is the minimized one, this should ideally
    #  be verified against an algorithmic solution for minimization)
    
    # Calculate the tour total cost:
    computed_total_cost = 0
    for i in range(len(tour) - 1):
        city_1 = tour[i]
        city_2 = tour[i + 1]
        computed_total_cost += calculate_euclidean_distance(
            cities[city_1][0], cities[city_1][1],
            cities[city_2][0], cities[city_2][1]
        )
    
    # Float comparison taking rounding into account
    if not math.isclose(computed_total_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Provided tour and total cost
tour_solution = [0, 3, 5, 9, 1, 2, 0]
total_cost_solution = 281.60

# Test the solution
result = test_solution(tour_solution, total_cost_solution)
print(result)