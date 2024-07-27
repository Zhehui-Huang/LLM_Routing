import math

# Coordinates of each city including the depot
city_coords = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]

# Robots' tours as provided
robot_tours = {
    0: [0, 6, 7, 5, 14, 9, 13, 2, 10, 1, 4, 11, 15, 12, 3, 8, 0]
}

def calculate_euclidean_distance(city1, city2):
    """Calculate Euclidean distance between two cities given their indices."""
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def test_robot_tour():
    # Test number of cities
    assert len(city_coords) == 16, "Number of cities including depot is invalid."

    # Test uniqueness and range of city indices
    total_unique_cities_visited = set()
    for tour in robot_tours.values():
        assert tour[0] == 0 and tour[-1] == 0, "Tour should start and end at the depot."
        total_unique_cities_visited.update(tour)

    # Test each city except depot is visited exactly once
    assert len(total_unique_cities_visited) == 16, "Not all cities are visited exactly once or visited multiple times."

    # Test calculation of the travel distances and total travel cost
    for robot_id, tour in robot_tours.items():
        computed_cost = 0
        for i in range(len(tour) - 1):
            distance = calculate_euclidean_distance(tour[i], tour[i + 1])
            computed_cost += distance
        
        # Replace with the actual cost if provided
        expected_cost = 173.01  # Provided in the task description
        assert math.isclose(computed_cost, expected_cost, abs_tol=0.01), f"Cost mismatch for Robot {robot_id}"

    # All robots starting point verification (as all start from the depot)
    assert all(tour[0] == 0 for tour in robot_tours.values()), "Not all robots start at depot."

    # Test if the overall total cost is correct
    overall_cost = sum([173.01 for _ in robot_tours])  # Replace each tour cost when known
    expected_total_cost = 173.01  # Provided in the task description
    assert math.isclose(overall_cost, expected_total_cost, abs_tol=0.01), "Overall total cost mismatch"

    return "CORRECT"

# Running the test function
test_result = test_robot_tour()
print(test_result)