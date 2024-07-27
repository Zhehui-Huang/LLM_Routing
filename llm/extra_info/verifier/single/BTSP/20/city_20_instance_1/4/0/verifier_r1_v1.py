import math

def calculate_euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def test_tour_requirements(cities, tour, expected_total_cost, expected_max_distance):
    # Check if all cities are visited exactly once and tour starts and ends at depot
    if sorted(tour) != sorted(list(range(len(cities))) + [0]):
        return "FAIL"
    
    # Calculate and check the total cost and maximum distance
    total_cost = 0
    max_distance = 0
    previous_city = tour[0]

    for current_city in tour[1:]:
        distance = calculate_euclidean_distance(cities[previous_city], cities[current_city])
        total_cost += distance
        if distance > max_distance:
            max_distance = distance
        previous_city = current_city
    
    if not math.isclose(total_cost, expected_total_cost, rel_tol=1e-2):
        return "FAIL"
    if not math.isclose(max_distance, expected_max_distance, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Define cities coordinates
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

# Run the test
result = test_tour_requirements(cities, tour, expected_total_cost, expected_max_distance)
print(result)