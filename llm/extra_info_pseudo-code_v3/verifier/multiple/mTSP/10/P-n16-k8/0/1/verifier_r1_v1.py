import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tours_and_costs(tours, city_coordinates):
    total_cost_calculated = 0.0
    visited_cities = set()

    for tour_info in tours:
        tour = tour_info['tour']
        provided_cost = tour_info['cost']

        # Check each tour starts and ends at the depot city 0
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Check that cities are visited exactly once across all robots, excluding the depot city (0)
        for city in tour[1:-1]:  # Exclude the first and the last because they are the depot
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)

        # Calculate and validate travel cost for the current tour
        tour_cost = 0.0
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i+1]
            tour_cost += calculate_euclidean_distance(*city_coordinates[city1], *city_coordinates[city2])

        total_cost_calculated += tour_cost

        if not math.isclose(tour_cost, provided_cost, rel_tol=1e-9):
            return "FAIL"

    # Check if all cities are visited exactly once, excluding the depot city
    if len(visited_cities) != len(city_coordinates) - 1:
        return "FAIL"

    # Check if overall cost is matched
    if not math.isclose(total_cost_calculated, sum(t['cost'] for t in tours), rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Constants
city_coords = [
    (30, 40), # depot
    (37, 52),
    (49, 49),
    (52, 64),
    (31, 62),
    (52, 33),
    (42, 41),
    (52, 41),
    (57, 58),
    (62, 42),
    (42, 57),
    (27, 68),
    (43, 67),
    (58, 48),
    (58, 27),
    (37, 69)
]

# Each robot's path and cost, adjusted from the earlier provided solution.
robot_tours = [
    {"tour": [0, 0], "cost": 0.00},
    {"tour": [0, 0], "cost": 0.00},
    {"tour": [0, 0], "cost": 0.00},
    {"tour": [0, 0], "cost": 0.00},
    {"tour": [0, 0], "cost": 0.00},
    {"tour": [0, 0], "cost": 0.00},
    {"tour": [0, 0], "cost": 0.00},
    {"tour": [0, 6, 2, 7, 5, 14, 9, 13, 8, 3, 12, 15, 11, 4, 10, 1, 0], "cost": 154.42}
]

verification_result = verify_tours_and_costs(robot_tours, city_coords)
print(verification_result)