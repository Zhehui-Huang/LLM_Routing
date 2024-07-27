import math

# Tours data defined by the given solution
robot_tours = {
    0: [0, 6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8],
}
robot_costs = {
    0: 140.56,
}

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Calculate distance between two cities
def calculate_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Test that each robot's tours are unique visits and check for meeting minimum visiting requirements
def test_each_city_visited_once():
    visited_cities = set()
    all_cities = set(cities.keys())
    for tour in robot_tours.values():
        visited_cities.update(tour)
    return all_cities == visited_cities

# Test the tour cost calculation
def test_calculated_tour_costs():
    calculated_costs = {}
    for id, tour in robot_tours.items():
        cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        calculated_costs[id] = round(cost, 2)
    return all(robot_costs[id] == calculated_costs[id] for id in robot_costs)

# Test the tour formation (checks if each city is visited exactly once)
def test_tour_formation():
    for tour in robot_tours.values():
        if any(tour.count(city) > 1 for city in tour):
            return False
    return True

# Check starting/ending on the designated depot
def test_start_end_depot():
    return all(tour[0] == 0 and tour[-1] == 8 for tour in robot_tours.values())  # Expected depots

# Check no tour serves only one customer node
def test_min_two_cities_visited():
    return all(len(set(tour) - {tour[0]}) >= 2 for tour in robot_tours.values())

# Run tests
def run_tests():
    if not test_each_city_visited_once():
        return "FAIL: Not all cities are visited exactly once"
    if not test_calculated_tour_costs():
        return "FAIL: Tour costs are miscalculated"
    if not test_tour_formation():
        return "FAIL: Invalid tour formation"
    if not test_start_end_depot():
        return "FAIL: Tour does not properly start/end at designated depot"
    if not test_min_two_cities_visited():
        return "FAIL: At least one tour visits fewer than two cities"
    return "CORRECT"

# Print test results
print(run_tests())