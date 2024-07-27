import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_travel_cost(tour, city_coords):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean(distance(city_coords[tour[i]], city_coords[tour[i+1]]))
    return total_cost

def test_solution():
    city_coords = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
        (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
        (45, 35)
    ]

    tours = [
        [0, 16, 1, 4, 11, 6, 20, 5, 7, 17, 14, 0],
        [0, 10, 12, 15, 3, 8, 18, 19, 13, 9, 2, 0]
    ]

    calculated_total_costs = []
    all_visited_cities = set()

    for tour in tours:
        cost = calculate_total_travel_cost(tour, city_coords)
        calculated_total_costs.append(cost)
        all_visited_cities.update(tour)

    correct_total_cost = sum(calculated_total_costs)
    expected_total_cost = 276.00

    # Check total travel cost
    if not math.isclose(correct_total_cost, expected_total_cost, rel_tol=1e-2):
        return "FAIL: Total cost mismatch"

    # Make sure all cities except the depot (0) are visited exactly once
    expected_cities = set(range(1, 21))
    visited_cities_without_depot = all_visited_cities - {0}
    if visited_cities_without_depot != expected_cities:
        return "FAIL: Not all cities are visited exactly once"

    # Check if each robot starts and finishes at the depot
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL: Tour does not start and end at deposit"

    return "CORRECT"

# Running the test
print(test_solution())