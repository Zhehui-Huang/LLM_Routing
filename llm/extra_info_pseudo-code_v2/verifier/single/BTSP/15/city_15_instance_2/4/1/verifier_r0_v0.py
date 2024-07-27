import math

# Coordinates of the cities in the format: city_index: (x, y)
city_coordinates = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40),
    4: (54, 42), 5: (36, 30), 6: (52, 82), 7: (93, 44),
    8: (21, 78), 9: (68, 14), 10: (51, 28),
    11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Provided solution data
tour = [0, 13, 6, 5, 11, 14, 11, 3, 7, 10, 7, 3, 6, 4, 8, 12, 9, 12, 1, 2, 4, 0, 0]
total_travel_cost = 935.24
maximum_distance = 54.41


def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city_coordinates[city1][0] - city_coordinates[city2][0]) ** 2 +
                     (city_coordinates[city1][1] - city_coordinates[city2][1]) ** 2)

def validate_tour():
    # Requirement 1 and 6: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit each city exactly once except the depot which must be visited twice
    city_visit_count = {i: tour.count(i) for i in range(15)}
    if city_visit_count[0] != 2:
        return "FAIL"
    if any(count != 1 for idx, count in city_visit_count.items() if idx != 0):
        return "FAIL"
    
    # Calculate the actual total travel cost and max distance
    calculated_cost = 0.0
    calculated_max_distance = 0.0
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(tour[i], tour[i + 1])
        calculated_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Requirement 7: Check the total travel cost
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-2):
        return "FAIL"
    
    # Requirement 8: Check the maximum distance between any two consecutive cities
    if not math.isclose(calculated_max_distance, maximum_distance, rel_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Execute the test function
print(validate_tour())