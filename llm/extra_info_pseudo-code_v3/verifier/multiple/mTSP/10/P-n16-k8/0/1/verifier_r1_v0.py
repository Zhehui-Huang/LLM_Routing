import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tours_and_costs(tours, city_coordinates):
    number_of_cities = len(city_coordinates)
    total_cost_calculated = 0.0
    visited_cities = set()

    for robot, tour in enumerate(tours):
        # Check each tour starts and ends at the depot city 0.
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        # Check that cities are visited exactly once across all robots, excluding the depot city (0).
        for city in tour[1:-1]:  # exclude the first and the last because they are depot
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)

        # Calculate travel cost for current tour.
        tour_cost = 0.0
        for i in range(len(tour) - 1):
            city1 = tour[i]
            city2 = tour[i + 1]
            tour_cost += calculate_euclidean_distance(*city_coordinates[city1], *city_coordinates[city2])

        total_cost_calculated += tour_cost

        # Check if provided tour costs are correct.
        if not math.isclose(tour_cost, tours[robot]["cost"], rel_tol=1e-9):
            return "FAIL"

    # Check if all cities are visited except the depot.
    if len(visited_cities) != number_of_cities - 1:
        return "FAIL"

    # Check if overall cost is correct.
    overall_cost_provided = sum(tour["cost"] for tour in tours)
    if not math.isclose(total_cost_calculated, overall_cost_provided, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Definitions and tours provided to test.
city_coords = [
    (30, 40), # Depot
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

# Tours and costs simulated from the provided solution.
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