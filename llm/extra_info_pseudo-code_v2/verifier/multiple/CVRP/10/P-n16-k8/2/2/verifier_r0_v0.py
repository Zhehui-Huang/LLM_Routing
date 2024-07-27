import math

# Given data and parameters
cities = {
    0: (30, 40, 0),
    1: (37, 52, 19),
    2: (49, 49, 30),
    3: (52, 64, 16),
    4: (31, 62, 23),
    5: (52, 33, 11),
    6: (42, 41, 31),
    7: (52, 41, 15),
    8: (57, 58, 28),
    9: (62, 42, 8),
    10: (42, 57, 8),
    11: (27, 68, 7),
    12: (43, 67, 14),
    13: (58, 48, 6),
    14: (58, 27, 19),
    15: (37, 69, 11)
}
robot_capacity = 35

# Robot tours and costs given in the solution
solution_tours = [
    [0, 14, 9, 13, 0],
    [0, 12, 15, 11, 0],
    [0, 3, 10, 0],
    [0, 5, 7, 0]
]
solution_costs = [82.73, 74.5, 65.57, 53.11]

def euclidean_distance(city1, city2):
    x1, y1, _ = cities[city1]
    x2, y2, _ = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_requirements():
    visited_demand = {key: 0 for key in cities.keys()}
    total_calculated_cost = 0

    # Requirement 1, 2, 3, 5, 6
    for tour, given_cost in zip(solution_tours, solution_costs):
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Requirement 1"

        total_demand = 0
        calculated_cost = 0

        for i in range(len(tour) - 1):
            total_demand += cities[tour[i]][2]
            visited_demand[tour[i]] += cities[tour[i]][2]
            calculated_cost += euclidean_distance(tour[i], tour[i+1])

        if total_demand > robot_capacity:
            return "FAIL: Requirement 2"

        if abs(calculated_cost - given_cost) > 0.01:  # Small margin for float comparison
            return "FAIL: Requirement 6: Mismatch in given and calculated tour costs"

        total_calculated_cost += calculated_cost
    
    # Requirement 3
    if any(visited_demand[city] != cities[city][2] for city in cities if city != 0):
        return "FAIL: Requirement 3"
    
    # Requirement 7
    if len(solution_tours) > 8:
        return "FAIL: Requirement 7"

    # Check against the overall travel cost (Requirement 4)
    given_total_cost = sum(solution_costs)
    if abs(total_calculated_school_cost - given_total_school_cost) > 0.01:
        return "FAIL: Requirement 4"

    return "CORRECT"

# Run the test
result = check_requirements()
print(result)