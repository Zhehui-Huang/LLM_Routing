import math

# Definition of city coordinates
city_coordinates = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 43),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35)
}

def calculate_euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_tour_cost(tour: list, coordinates: dict):
    """Calculate the total travel cost of a given tour."""
    total_cost = 0
    last_city = tour[0]
    for city in tour[1:]:
        total_cost += calculate_euclidean_distance(coordinates[last_city], coordinates[city])
        last_city = city
    return total_cost

# Tours and costs from the provided solution
robots_tours_costs = [
    ([0, 6, 18, 7, 15, 8, 16, 12, 10, 11, 0], 148.62767754005085),
    ([0, 1, 4, 14, 3, 17, 9, 2, 5, 13, 0], 152.52152945750305)
]
overall_total_cost_provided = 301.1492069975539

def test_solution(robots_tours_costs, overall_total_cost_provided, city_coordinates):
    # Collect all city visits excluding depots:
    all_cities_visited = set()
    overall_computed_cost = 0

    # Check each robot's tour and compute costs
    for tour_info in robots_tours_num_costs:
        tour, given_cost = tour_info
        # Ensures starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        computed_cost = calculate_tour_cost(tour, city_coordinates)
        # Verify cost with reasonable rounding precision
        if not math.isclose(computed_cost, given_cost, abs_tol=0.01):
            return "FAIL"
        # Adding city visits
        all_cities_visited.update(tour[1:-1])  # Exclude the depot (start and end)
        overall_computed_cost += computed_cost
    
    # Check if all cities are covered exactly once
    if len(all_cities_visited) != 18 or all_cities_visited != set(range(1, 19)):
        return "FAIL"
    
    # Check overall total cost with reasonable rounding precision
    if not math.isclose(overall_computed_cost, overall_total_cost_provided, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# Run the tests
result = test_solution(robots_tours_costs, overall_total_cost_provided, city_coordinates)
print(result)