import math

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Cities and their coordinates (index corresponds to city number)
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Tours provided in the solution
robot_tours = [
    [0, 9, 0],
    [1, 14, 1],
    [2, 14, 2],
    [3, 14, 3],
    [4, 14, 4],
    [5, 11, 5],
    [6, 11, 6],
    [7, 11, 7]
]

def verify_tours(robot_tours):
    # Check if each city is visited exactly once
    visited_cities = set()
    for tour in robot_tours:
        visited_cities.update(tour[1:-1])  # Ignore depots at the start and end

    if len(visited_cities) != 8:  # We should exactly visit cities 8 through 15 once
        return "FAIL"

    # Verify that each tour starts and ends at its depot
    for i, tour in enumerate(robot_tours):
        if tour[0] != i or tour[-1] != i:
            return "FAIL"

    # Compute and verify the total distance
    total_cost_calculated = 0
    provided_costs = [64.1248781675256, 65.29931086925804, 47.53945729601885, 74.96665925596525,
                      88.40814442120137, 86.02325267042627, 61.773780845922005, 73.59347797189639]
    for tour, provided_cost in zip(robot_tours, provided_costs):
        tour_cost = sum(calculate_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
        if not math.isclose(tour_cost, provided + cost, abs_tol=0.001):
            return "FAIL"
        total_cost_calculated += tour_cost

    if not math.isclose(total_cost_calculated, 561.7289614982137, abs_tol=0.001):
        return "FAIL"

    return "CORRECT"

# Check the solution
print(verify_tours(robot_tours))