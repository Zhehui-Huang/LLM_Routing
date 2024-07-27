import numpy as np

# Coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 66), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Tours provided in the solution
robots_tours = [
    [0, 18, 19, 0], [0, 8, 18, 0], [0, 3, 19, 0], [0, 8, 19, 0], 
    [0, 3, 18, 0], [0, 3, 8, 0], [0, 14, 17, 0], [0, 9, 17, 0],
    [0, 9, 13, 0], [0, 12, 19, 0]
]

# Compute Euclidean distance
def compute_distance(c1, c2):
    return np.sqrt((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2)

# Check if all demands are met
def check_demands(robots_tours, demands):
    delivery = [0] * len(demands)
    for tour in robots_tours:
        for i in range(1, len(tour)-1):
            delivery[tour[i]] += demands[tour[i]]
    return all(delivery[i] >= demands[i] for i in range(1, len(demands)))

# Check if robots return to the depot
def check_return_to_depot(robots_tours):
    return all(tour[0] == 0 and tour[-1] == 0 for tour in robots_tours)

# Check the robots capacity
def check_capacity(robots_tours, demands, max_capacity=160):
    for tour in robots_tours:
        load = sum(demands[city] for city in tour[1:-1])
        if load > max_capacity:
            return False
    return True

# Check requirements
def check_solution(robots_tours, demands, coordinates):
    if not check_return_to_depot(robots_tours):
        return "FAIL: Problem with robot return to depot."
    if not check_demands(robots_tours, demands):
        return "FAIL: Problem with demands not being fully met."
    if not check_capacity(robots_tours, demands):
        return "FAIL: Problem with robot capacity exceeded."
    return "CORRECT"

# Invoke the check
result = check_solution(robots_tours, demands, coordinates)
print(result)