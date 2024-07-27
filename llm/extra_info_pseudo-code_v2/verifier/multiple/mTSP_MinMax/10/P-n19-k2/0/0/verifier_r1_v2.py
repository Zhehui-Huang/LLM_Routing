import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(cities, robot_tours, expected_costs, max_expected_cost):
    visited_cities = set()
    all_tour_costs = []

    for tour in robot_tours:
        # Validate start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Track visited cities and calculate travel costs
        tour_cost = 0
        for i in range(len(tour) - 1):
            if tour[i] != tour[i+1]:  # Ignore zero-length trips
                tour_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
                if tour[i+1] != 0:  # Skip depot city for visited checking
                    visited_cities.add(tour[i+1])

        all_tour_costs.append(tour_cost)

        # Check against individually provided costs
        if not math.isclose(tour_cost, expected_costs[robot_tours.index(tour)], rel_tol=1e-5):
            return "FAIL"

    # Validate every non-depot city was visited
    if len(visited_cities) != len(cities) - 1:  # Exclude depot
        return "FAIL"

    # Check the maximum travel cost condition
    if not math.isclose(max(all_tour_costs), max_expected_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Test data
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

robot_tours = [
    [0, 1, 4, 11, 10, 8, 9, 15, 7, 2, 18, 6, 0],
    [0, 14, 12, 3, 17, 16, 13, 5, 0]
]
expected_costs = [135.5594779741043, 131.6036792731059]
max_expected_cost = 135.5594779741043

result = verify_solution(cities, robot_tourstraditionally waiting, watched_costs, maximal)pected_cost)
print(result)