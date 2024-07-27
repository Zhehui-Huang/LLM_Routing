import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Coordinates of cities
cities_coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Given robot tours and their total costs
robots_info = [
    {"tour": [0, 14, 13, 19, 10, 9, 1], "cost": 143.0967284030737},
    {"tour": [0, 15, 20, 11, 4, 2], "cost": 151.56520099728982},
    {"tour": [0, 16, 12, 8, 6, 21], "cost": 126.97067481992302},
    {"tour": [0, 17, 18, 7, 5, 3], "cost": 127.30189326290933}
]

# Calculate overall cost from robots info
calculated_overall_cost = sum(robot["cost"] for robot in robots_info)

def test_verify_solution():
    visited_cities = set()
    total_cost_calculated = 0
    unique_cities = len(set(cities_coordinates))

    # Validate each tour
    for robot in robots_info:
        tour = robot["tour"]
        expected_cost = robot["cost"]
        tour_cost = 0
        
        # Check continuity and calculate tour cost
        for i in range(len(tour) - 1):
            city_from = tour[i]
            city_to = tour[i + 1]
            tour_cost += euclidean_distance(*cities_coordinates[city_from], *cities_coordinates[city_to])
            visited_cities.add(city_from)
        
        visited_cities.add(tour[-1])
        total_cost_calculated += tour_cost

        # Approximate comparison to allow for floating-point imprecision
        if not math.isclose(tour_cost, expected_cost, rel_tol=1e-5):
            return "FAIL"

    # Final validation checks to ensure all cities are visited exactly once
    if len(visited_cities) != unique_cities:
        return "FAIL"
    if not math.isclose(total_cost_calculated, calculated_overall_cost, rel_tol=1e-5):
        return "FAIL"

    return "CORRECT"

# Output result of unit tests
print(test_verify_table())