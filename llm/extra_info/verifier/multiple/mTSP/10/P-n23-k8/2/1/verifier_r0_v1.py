import math

# City coordinates where index is the city number
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Tours for each robot as specified in the solution
robots_tours = [
    [0, 21, 16, 6, 0],
    [0, 1, 20, 10, 0],
    [0, 2, 4, 7, 0],
    [0, 5, 22, 11, 0],
    [0, 13, 15, 12, 0],
    [0, 14, 17, 9, 0],
    [0, 8, 3, 0],
    [0, 18, 19, 0]
]

# Given costs are used for verification
given_costs = [29.9, 75.69, 94.95, 99.35, 95.11, 78.7, 72.82, 89.42]
overall_cost = 635.94

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tours, given_costs, overall_cost):
    total_calculated_cost = 0
    visited_cities = set()

    # Check tours and costs
    for idx, tour in enumerate(tours):
        tour_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        if not math.isclose(tour_cost, given_costs[idx], abs_tol=0.01):
            print(f"Cost mismatch for Robot {idx}: calculated={tour_cost}, expected={given_costs[idx]}")
            return "FAIL"
        total_calculated_cost += tour_cost
        visited_cities.update(tour)

    # Check overall cost
    if not math.isclose(total_calculated_cost, overall_cost, abs_tol=0.01):
        print(f"Overall cost mismatch: calculated={total_calculated_cost}, expected={overall_cost}")
        return "FAIL"

    # Check city visits, excluding duplicate depot visits
    if visited_cities != set(cities.keys()):
        print("Not all cities are visited exactly once.")
        return "FAIL"

    # Everything passed
    return "CORRECT"

result = verify_solution(robots_tours, given_costs, overall_cost)
print(result)