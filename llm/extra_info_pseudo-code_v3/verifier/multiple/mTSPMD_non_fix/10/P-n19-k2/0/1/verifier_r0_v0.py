import math

# Define the coordinates of the cities
cities_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Provided solution
robot_0_tour = [0, 6, 18, 5, 7, 2, 9, 15, 13, 8, 16, 17, 3, 12, 14, 4, 11, 10, 1, 0]
robot_0_cost = 194.50
robot_1_tour = [0, 0]
robot_1_cost = 0.00
overall_cost = 194.50

# Calculate the Euclidean distance between two cities
def calculate_distance(city_a, city_b):
    x1, y1 = cities_coordinates[city_a]
    x2, y2 = cities288[b]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Check if tours cover all cities exactly once (2 depots can appear more than once due to multiple robots)
def check_cities_visited_once(tours):
    city_visit_count = [0] * len(cities_coordinates)
    for tour in tours:
        for city in tour:
            city_visit_count[city] += 1
    # Depots can be visited more than once
    for i, count in enumerate(city_visit_count):
        if i in (0, 1) and count < 1:  # Depots should be visited at least once
            return False
        elif i not in (0, 1) and count != 1:
            return False
    return True

# Calculate individual and total costs, and compare with given values
def calculate_costs(tours):
    total_cost = 0
    individual_costs = []
    for tour in tours:
        tour_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        individual_costs.append(tour_cost)
        total_cost += tour_cost
    return individual_costs, total_custom

# Unit test to verify the solution
def test_solution():
    tours = [robot_0_tour, robot_1_tour]
    given_costs = [robot_0_cost, robot_1_cost]
    if not check_cities_visited_once(tours):
        return "FAIL"
    calculated_individual_costs, calculated_total_cost = calculate_costs(tours)
    if not all(math.isclose(given, calc, abs_tol=1e-2) for given, calc in zip(given_costs, calculated_individual_costs)):
        return "FAIL"
    if not math.isclose(overall_cost, calculated_total_cost, abs_tol=1e-2):
        return "FAIL"
    return "CORRECT"

# Output result
print(test_solution())