import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tours, costs, cities_coordinates):
    # Check if all cities are visited exactly once
    visited = set()
    for tour in tours:
        visited.update(tour[1:-1])  # Exclude depots from the first and last index for re-visit

    if len(visited) != 15:  # 23 cities total - 8 depots = 15 must be visited (excluding depots)
        return "FAIL"
    
    # Verify if each robot starts and ends at its assigned depot
    for i, tour in enumerate(tours):
        if tour[0] != tour[-1] or tour[0] != i:
            return "FAIL"

    # Calculate costs and compare with provided costs
    total_calculated_cost = 0
    for idx, (tour, cost) in enumerate(zip(tours, costs)):
        calculated_cost = 0
        for j in range(len(tour) - 1):
            city1 = tour[j]
            city2 = tour[j + 1]
            calculated_cost += calculate_euclidean_distance(*cities_coordinates[city1], *cities_coordinates[city2])
        calculated_cost = round(calculated_cost, 2)
        total_calculated_cost += calculated_cost

        # Check if individual tour costs match
        if abs(calculated_cost - cost) > 0.01:  # Allowing small floating point error
            return "FAIL"

    # Check overall total cost
    if abs(total_calculated_cost - sum(costs)) > 0.01:
        return "FAIL"

    return "CORRECT"

# Defined Constants
cities_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

provided_tours = [
    [0, 19, 0],
    [1, 16, 1],
    [2, 13, 2],
    [3, 20, 3],
    [4, 8, 4],
    [5, 15, 5],
    [6, 14, 6],
    [7, 22, 21, 12, 17, 11, 9, 10, 18, 7]
]

provided_costs = [87.86, 12.17, 18.11, 59.67, 52.61, 78.0, 42.52, 260.74]

# Calling verification function
result = verify_solution(provided_tours, provided_costs, cities_coordinates)
print(result)