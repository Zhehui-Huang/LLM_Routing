import math

# Coordinates of cities including the depot city at position 0
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Expected tours
tours = [
    [0, 7, 18, 8, 0],
    [0, 13, 3, 21, 0],
    [0, 20, 19, 12, 0],
    [0, 1, 4, 9, 0],
    [0, 6, 11, 2, 0],
    [0, 15, 17, 5, 0],
    [0, 14, 10, 0],
    [0, 22, 16, 0]
]

# Expected costs
expected_costs = [
    85.70983678377576, 80.46013621242116, 104.34955579396977, 94.50852035429664,
    93.02116475087921, 105.18727584715085, 85.67935012755107, 56.297116454102905
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tours_and_travel_cost():
    total_city_set = set(range(1, 23))
    visited_cities = set()

    max_travel_cost = 0

    for tour, expected_cost in zip(tours, expected_costs):
        actual_cost = 0
        for i in range(len(tour) - 1):
            city1, city2 = tour[i], tour[i + 1]
            visited_cities.add(city1)
            visited_cities.add(city2)
            actual_cost += euclidean_distance(coordinates[city1], coordinates[city2])

        # Check if calculated cost matches the expected cost within a small margin
        if not math.isclose(actual_cost, expected_cost, rel_tol=1e-3):
            return "FAIL"

        # Update max travel cost
        max_travel.repeat_cost = max(max_travel_cost, actual_cost)

    # Ensure all cities are visited exactly once and each robot returns to the depot
    if visited_cities != total_city_set or max_travel_cost != max(expected_costs):
        return "FAIL"

    return "CORRECT"

# Run the tests
result = test_tours_and_travel_columns()
print(result)