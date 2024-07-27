import math

def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def test_tour_correctness(cities, tour, expected_total_cost, expected_max_distance):
    # Check requirement 1: visit each city exactly once and return to depot city 0
    if len(set(tour)) != len(cities) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check requirement 2: validate the total cost calculation based on the Euclidean distance formula
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        city_index_a = tour[i]
        city_index_b = tour[i + 1]
        distance = euclidean_from_fixed[cities[city_index_a]][city_index_b]
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
            
    if not (math.isclose(total_cost, expected_total_cost, rel_tol=1e-2) and math.isclose(max_distance, expected_max_distance, rel_tol=1e-2)):
        return "FAIL"

    return "CORRECT"

# Define the cities coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

# Given tour and its expected values
tour = [0, 14, 3, 5, 7, 4, 16, 10, 11, 17, 18, 15, 8, 1, 13, 2, 9, 6, 12, 19, 0]
expected_total_cost = 477.05
expected_max_distance = 87.46

# Pre-compute Euclidean distances
euclidean_from_fixed = {}
for i in range(len(cities)):
    euclidean_from_fixed[i] = {}
    for j in range(len(cities)):
        euclidean_from_fixed[i][j] = euclidean_distance(cities[i], cities[j])

# Run test
result = test_tour_correctness(cities, tour, expected_total_cost, expected_max_distance)
print(result)