import math

# City coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

# Simulated output
robot_tours = {
    0: [0, 0, 2, 7, 9, 15, 13, 10, 3, 16, 11, 0],
    1: [0, 6, 1, 4, 14, 12, 8, 17, 5, 0]
}
costs = {
    0: 168.42642600573245,
    1: 141.23377839360984
}

# Verify the solution
def calculate_euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

def verify_requirements(tours, costs):
    # Requirement 2 & 3
    visited_cities = set()
    for robot in tours:
        if tours[robot][0] != 0 or tours[robot][-1] != 0:
            return "FAIL"  # Tours must start and end at the depot
        visited_cities.update(tours[robot][1:-1])
    
    # Requirement 3
    if visited_cities != set(range(1, 19)):  
        return "FAIL"  # Must include all cities except the depot, visited once

    # Requirement 4 & 5
    for robot in tours:
        computed_cost = 0
        tour = tours[robot]
        for i in range(len(tour) - 1):
            computed_cost += calculate_euclidean_distance(tour[i], tour[i + 1])
        if not math.isclose(computed_cost, costs[robot], rel_tol=1e-5):
            return "FAIL"  # Check total travel cost

    # Requirement 7
    overall_cost = sum(costs.values())
    if not math.isclose(overall_cost, 309.6602043993423, rel_tol=1e-5):
        return "FAIL"  # Overall cost validation

    return "CORRECT"

# Execute verification
result = verify_requirements(robot_tours, costs)
print(result)