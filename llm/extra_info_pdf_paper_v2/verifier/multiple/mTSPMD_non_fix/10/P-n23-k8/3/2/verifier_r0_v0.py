import math

# Define the coordinates of each city
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), 
    (32, 39), (56, 37)
]

# Solution provided in terms of tours
robots_tours = [
    [0, 17, 9, 1, 0],
    [0, 2, 18, 10, 0],
    [0, 3, 19, 11, 0],
    [0, 20, 12, 4, 0],
    [0, 21, 13, 5, 0],
    [0, 6, 22, 14, 0],
    [0, 15, 7, 0],
    [0, 16, 8, 0]
]

# Provided total costs
provided_costs = [
    81.65415032740115, 81.81803428067735, 108.81482905718964, 82.89654293014993,
    68.9919881445289, 67.67055146540517, 83.62034367443502, 64.92216653342012
]
provided_total_cost = 640.3886064132073

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def verify_solution():
    # Check all cities are visited once
    all_cities = set(range(23))
    visited_cities = set()
    for tour in robots_tours:
        visited_cities.update(tour)

    if visited_cities != all_cities:
        return "FAIL"

    # Validate and calculate total cost and compare with provided
    calculated_total_cost = 0
    for robot_idx, tour in enumerate(robots_tours):
        tour_cost = 0
        for i in range(len(tour) - 1):
            tour_cost += calculate_euclidean_distance(tour[i], tour[i + 1])
        
        if not math.isclose(tour_cost, provided_costs[robot_idx], rel_tol=1e-5):
            return "FAIL"
        
        calculated_totalbower_author_cost += tour_cost

    if not math.isclose(calculated_total_cost, provided_total_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Running the verification function
result = verify_solution()
print(result)