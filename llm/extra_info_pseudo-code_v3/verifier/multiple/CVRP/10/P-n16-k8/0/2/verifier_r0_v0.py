import math

# Example tour and demand data (must be replaced with actual test/output data).
# Each list inside tours represents the cities visited by each robot in sequence.
tours = [
    [0, 6, 12, 0],  # Robot 0
    [0, 1, 5, 14, 0],  # Robot 1
    [0, 2, 8, 13, 0],  # Robot 2
    [0, 3, 10, 0],  # Robot 3
    [0, 4, 11, 15, 0],  # Robot 4
    [0, 7, 0],  # Robot 5
    [0, 9, 0],  # Robot 6
    [0, 0]
]

# Total number of cities and their demand
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Checking constraints
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_tour_starts_and_ends_at_depot(tours):
    return all(tour[0] == 0 and tour[-1] == 0 for tour in tours)

def check_cities_visited_exactly_once_except_depot(tours):
    city_visits = [0] * 16  # Considering 16 cities including the depot
    for tour in tours:
        for city in tour:
            city_visits[city] += 1
    # Each city except the depot should be visited exactly once
    return all(v == 1 for i, v in enumerate(city_visits) if i != 0)

def check_capacity_constraints(tours, demands):
    for tour in tours:
        load = sum(demands[city] for city in tour)
        if load > 35:
            return False
    return True

def test_solution(tours, demands):
    if not check_tour_starts_and_ends_at_depot(tours):
        return "FAIL: Tours must start and end at the depot."
    if not check_cities_visited_exactly_once_except_depot(tours):
        return "FAIL: Each city must be visited exactly once."
    if not check_capacity_constraints(tours, demands):
        return "FAIL: Capacity constraints are violated."

    return "CORRECT"

# Execute tests
print(test_solution(tours, demands))