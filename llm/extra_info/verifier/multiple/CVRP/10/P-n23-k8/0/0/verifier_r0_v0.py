import math

# Data
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
          (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
          (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), 
          (32, 39), (56, 37)]

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robot_capacity = 40

# Solution Provided
solution = [
    {'tour': [0, 21, 16, 1, 10, 13, 0], 'cost': 72.08744208476426},
    {'tour': [0, 6, 20, 19, 0], 'cost': 101.15233190761194},
    {'tour': [0, 2, 22, 0], 'cost': 61.088744687683246},
    {'tour': [0, 4, 11, 9, 0], 'cost': 104.8967158934193},
    {'tour': [0, 7, 5, 12, 0], 'cost': 95.16037446322657},
    {'tour': [0, 15, 3, 0], 'cost': 78.20189727339391},
    {'tour': [0, 14, 18, 0], 'cost': 106.500359623892},
    {'tour': [0, 17, 0], 'cost': 63.56099432828282}
]

# Validate Solution
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

def validate_solution():
    # Check demands are met
    served = [0] * len(demands)
    for sol in solution:
        load = 0
        for i in range(1, len(sol['tour']) - 1):
            city = sol['tour'][i]
            served[city] += demands[city]
            load += demands[city]
        if load > robot_capacity:
            return "FAIL: Capacity Exceeded"

    if any(served[i] != demands[i] for i in range(1, len(demands))):
        return "FAIL: Demand Not Matched Correctly"

    # Validate tour cost calculation
    for sol in solution:
        calc_cost = 0
        for i in range(len(sol['tour']) - 1):
            calc_cost += euclidean_distance(sol['tour'][i], sol['tour'][i + 1])
        if not math.isclose(sol['cost'], calc_cost, rel_tol=1e-5):
            return "FAIL: Cost Mismatch"

    # Validate all costs summarized
    total_cost = sum(sol['cost'] for sol in solution)
    if not math.isclose(total_cost, 682.6488602622741, rel_tol=1e-5):
        return "FAIL: Total Cost Mismatch"

    return "CORRECT"

# Run validation
print(validate_solution())