import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost, cities):
    # Constants for requirements
    REQUIRED_CITIES_COUNT = 13

    # Check if the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if the tour includes exactly 13 cities
    if len(set(tour)) != REQUIRED_CITIES_COUNT:
        return "FAIL"

    # Check if all cities in the tour are from the given set and if the city indices are valid
    if any(city not in cities for city in tour):
        return "FAIL"

    # Calculating the total travel cost from the tour provided
    calculated_total_cost = 0
    for i in range(len(tour)-1):
        city_index_1 = tour[i]
        city_index_2 = tour[i+1]
        calculated_total_cost += calculate_euclidean_distance(cities[city_index_1][0], cities[city_index_1][1],
                                                              cities[city_index_2][0], cities[city_index_2][1])
    
    # Check if the calculated cost is close to the provided total cost with a small margin of error
    if not math.isclose(calculated_total_cost, total_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Example input data for verification
cities_coordinates = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Provided solution data
tour = [0, 1, 10, 4, 7, 12, 18, 13, 6, 5, 17, 15, 3, 0]
total_cost = 275.0799284989127

# Perform the verification
test_result = verify_solution(tour, total_cost, cities_coordinates)
print(test_result)