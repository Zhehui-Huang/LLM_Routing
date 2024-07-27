import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# City coordinates map
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

# Expected solution results
robot_0_tour = [0, 6, 2, 7, 5, 9, 8, 3, 1, 4, 0]
robot_1_tour = [0, 18, 13, 15, 16, 17, 12, 14, 11, 10, 0]

# Expected travel costs
expected_cost_robot_0 = 121.84817612829175
expected_cost_robot_1 = 149.76726379384303

# Calculate tour cost
def calculate_tour_cost(tour, cities_coordinates):
    total_cost = 0.0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        total_cost += calculate_euclidean distance(
            cities_coordinates[city1][0], cities_coordinates[city1][1],
            cities_coordinates[city2][0], cities_coordinates[city2][1]
        )
    return total_cost

# Calculate actual costs
actual_cost_robot_0 = calculate_tour_cost(robot_0_tour, city_coordinates)
actual_cost_robot_1 = calculate_tour_cost(robot_1_tour, city_coordinates)

# Test individual requirements
def test_robot_tour_starts_and_ends_at_depot(robot_tour):
    return robot_tour[0] == 0 and robot_tour[-1] == 0

def test_all_cities_visited_once_excluding_depot(all_tours, total_cities):
    visited = [0] * total_cities
    for tour in all_tours:
        for city in tour[1:-1]:  # exclude start/end depot city
            visited[city] += 1
    return all(v == 1 for idx, v in enumerate(visited) if idx != 0)

def test_city_count(excluding_depot, actual_count):
    return excluding_depot == actual_count

def tests():
    tours = [robot_0_tour, robot_1_tour]
    all_tours_correct = all(test_robot_tour_starts_and_ends_at_depot(tour) for tour in tours)
    all_cities_visited_once = test_all_cities_visited_once_excluding_depot(tours, len(city_coordinates))
    city_count_correct = test_city_count(18, sum(1 for k in city_coordinates if k != 0))
    
    costs_are_correct = math.isclose(actual_cost_robot_0, expected_cost_robot_0) and math.isclose(actual_cost_robot_1, expected_cost_robot_1)
    total_cost_correct = math.isclose(actual_cost_robot_0 + actual_cost_robot_1, 271.6154399221348)
    
    if all_tours_correct and all_cities_visited_once and city_count_correct and costs_are_correct and total_cost_correct:
        return "CORRECT"
    else:
        return "FAIL"

# Run tests
output = tests()
print(output)